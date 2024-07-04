from medical_data_visualizer import load_and_process_data, draw_cat_plot, draw_heat_map

# Cargar y procesar los datos
file_path = 'medical_examination.csv'  # Asegúrate de tener el archivo en el mismo directorio
df = load_and_process_data(file_path)

# Generar y guardar los gráficos
cat_plot_fig = draw_cat_plot(df)
heat_map_fig = draw_heat_map(df)
