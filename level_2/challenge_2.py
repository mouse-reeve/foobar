''' Model infections that pass to neighbors on x or y axis of 2D matrix '''

def answer(population, x, y, strength):
    ''' recursively model infection path '''
    if population[y][x] <= strength:
        population[y][x] = -1

        neighbors = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]
        for coord in neighbors:
            if 0 <= coord[0] < len(population) and 0 <= coord[1] < len(population[0]) \
                    and population[coord[0]][coord[1]] != -1:
                population = answer(population, coord[1], coord[0], strength)
    return population
