# 105demography

Population and regression analysis.

Project for semester 1 of the Epitech Math module.

### Description

This project predicts future population growth using historical data. It performs linear regression to estimate:

1. Population predictions for 2050.
2. Coefficients and root-mean-square deviations for regression fits.
3. Correlation between year and population.

## Getting Started

### Dependencies

- [Python3](https://python.org/)

### Installation

* Download/Clone the repository and enter its directory.
* Now you are ready to run the code.

## Usage

**Execution:** `./105demography [code]+`

### Arguments
- **`code`**: Country code(s) for regression analysis.

### Examples

To analyze the European Union:
```
$> ./105demography EUU
Country: European Union
Fit1
Y = 1.62 X - 2749.67
Root-mean-square deviation: 5.22
Population in 2050: 570.85
Fit2
X = 0.60 Y + 1707.97
Root-mean-square deviation: 5.32
Population in 2050: 574.54
Correlation: 0.9820
```

To analyze Bolivia, Brazil, and Peru:
```
$> ./105demography BOL BRA PER
Country: Bolivia, Brazil, Peru
Fit1
Y = 3.06 X - 5906.34
Root-mean-square deviation: 2.22
Population in 2050: 359.35
Fit2
X = 0.33 Y + 1932.53
Root-mean-square deviation: 2.22
Population in 2050: 359.70
Correlation: 0.9991
```

## Acknowledgments

* [Epitech](https://www.epitech.eu/)

## Authors

* **Daniel Sanchez** ([GitHub](https://github.com/angsanch) / [LinkedIn](https://www.linkedin.com/in/angeldanielsanchez/))

## License

This project is licensed under the GNU Public License version 3.0 - see the [LICENSE](LICENSE) file for details.
