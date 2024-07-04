import unittest
import pandas as pd
from medical_data_visualizer import load_and_process_data, draw_cat_plot, draw_heat_map

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = 'medical_examination.csv'
        self.df = load_and_process_data(self.file_path)

    def test_load_and_process_data(self):
        df = load_and_process_data(self.file_path)
        self.assertEqual(df.shape[1], 14)  # Verificar el número de columnas
        self.assertIn('overweight', df.columns)  # Verificar que la columna 'overweight' exista

    def test_draw_cat_plot(self):
        fig = draw_cat_plot(self.df)
        self.assertIsNotNone(fig)

    def test_draw_heat_map(self):
        fig = draw_heat_map(self.df)
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
