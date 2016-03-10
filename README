# foo - Find the Optimal Order

Pyomo python program to calculate optimal order from websites including shipping costs (MILP)

## Dependencies

* Install [`glpk`](https://www.gnu.org/software/glpk/)

        brew install glpk # osx

* [Anaconda 2.7](https://www.continuum.io/downloads)

Clone this repository

* Open a terminal
* Change directory to where you would like to clone this repository

    cd ~/GitRepos/
    git clone https://github.com/kdheepak89/foo.git

#### Environment

The below will create a python environment called `foo-env`.
If you want a different environment name, open `environment.yml` and change the first line

Open a terminal and run the following

    cd ~/GitRepos/foo # Or change directory to the root of the folder
    conda env create -f environment.yml

## Run

#### Activate the environment

* Open a terminal, and change directory to the root of the folder
* Run the following to activate an environment

    source activate foo-env

* Run the following to find the optimal order using input in a folder

    python foo/run.py --folder foo/data

OR

* Run the following to find the optimal order using input from individual files

    python foo/run.py --quantity foo/data/quantity.csv --price foo/data/price.csv --shipping foo/data/shipping.csv


Three files are required to find the optimal order

* prices.csv
* quantity.csv
* shipping.csv

Prices contains the price of an item when purchased from a website
Quantity contains the number of items required
Shipping contains the shipping cost from the individual websites

## Troubleshooting

* Names of items in quantity.csv has to match prices.csv
* Names of websites in shipping.csv has to match prices.csv
* Remove all empty lines
