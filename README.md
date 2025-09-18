# Commands:

## Run pytest:
`
python -m pytest -v TestShippingCalculator.py
`

## Run coverage:
`
python -m coverage run -m pytest TestShippingCalculator.py
python -m coverage report -m
`

## Run coverage with branch mode:

python -m coverage run --branch -m pytest TestShippingCalculator.py
python -m coverage report -m
