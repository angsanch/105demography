#!/usr/bin/python3
##
## EPITECH PROJECT, 2023
## stats.py
## File description:
## math
##

def sum_populations(country_list):
    pop = []
    for i in range(len(country_list[0]["population"])):
        year = 0
        for country in country_list:
            year += country["population"][i]
        pop.append(year)
    return pop

def estimate_y(data, x):
    return data["xa"] * x + data["xb"]

def estimate_x(data, y):
    return (y - data["yb"]) / data["ya"]

def srmd(stats, x, y):
    stats["dx"] = (sum([(y[i] - estimate_y(stats, x[i])) ** 2 \
        for i in range(len(x))]) / stats["n"]) ** 0.5
    stats["dy"] = (sum([(y[i] - estimate_x(stats, x[i])) ** 2 \
        for i in range(len(x))]) / stats["n"]) ** 0.5
    return stats

def make_stats(x, y):
    if len(x) != len(y):
        raise Exception("Lengths must be equal")
    stats = {"Exy": sum([x[i] * y[i] for i in range(len(x))]),
        "Ex": sum(x),
        "Ey": sum(y),
        "Ex2": sum(i * i for i in x),
        "Ey2": sum(i * i for i in y),
        "n": len(x)}
    divisor = (stats["n"] * stats["Ex2"]) - (stats["Ex"] ** 2)
    stats["xa"] = ((stats["n"] * stats["Exy"]) - (stats["Ex"] * \
        stats["Ey"])) / divisor
    stats["xb"] = ((stats["Ey"] * stats["Ex2"]) - (stats["Ex"] * \
        stats["Exy"])) / divisor
    divisor = (stats["n"] * stats["Ey2"]) - (stats["Ey"] ** 2)
    stats["ya"] = ((stats["n"] * stats["Exy"]) - (stats["Ex"] * \
        stats["Ey"])) / divisor
    stats["yb"] = ((stats["Ex"] * stats["Ey2"]) - (stats["Ey"] * \
        stats["Exy"])) / divisor
    stats["r"] = ((stats["n"] * stats["Exy"]) - (stats["Ex"] * stats["Ey"])) /\
        (((stats["n"] * stats["Ex2"]) - (stats["Ex"] ** 2)) * \
        (((stats["n"] * stats["Ey2"]) - (stats["Ey"] ** 2)))) ** 0.5
    return srmd(stats, x, y)
