min_population = df.population.min()
df[
    df['population'] == min_population
].households.max()
