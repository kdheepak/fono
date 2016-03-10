from pyomo.environ import *
import ReferenceModel

def solve(instance, solver='glpk', mipgap=0.01):
    solver = SolverFactory(solver)
    solver.options['mipgap'] = mipgap
    instance.preprocess()
    _results = solver.solve(instance, suffixes=['dual'])
    instance.solutions.store_to(_results)
    return(_results)

def display(_results):
    for i in _results['Solution']:
        print("Objective value = {}".format(i['Objective']['Objective']['Value']))

    solution = _results['Solution'][0]
    for item in sorted(solution['Variable'].iteritems()):
        print("{}: {}".format(item[0], item[1]['Value']))


if __name__ == '__main__':

    price = {
        ('website1', 'item1'): 1, # dollars
        ('website2', 'item1'): 2, # dollars
        ('website1', 'item2'): 1, # dollars
        ('website2', 'item2'): 2, # dollars
        ('website1', 'item3'): 1, # dollars
        ('website2', 'item3'): 2, # dollars
        ('website1', 'item4'): 1, # dollars
        ('website2', 'item4'): 2, # dollars
        ('website1', 'item5'): 1, # dollars
        ('website2', 'item5'): 2, # dollars
            }

    quantity = {
        'item1': 10, # number of items
        'item2': 0, # number of items
        'item3': 0, # number of items
        'item4': 0, # number of items
        'item5': 0, # number of items
               }

    shipping = {
        'website1': 21,
        'website2': 10
    }

    model = ReferenceModel.create_model(price, quantity, shipping)

    display(solve(model))
