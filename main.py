import argparse
import json


def parse_args():
    '''
    Parse command line arguments
    '''
    parser = argparse.ArgumentParser(description='Testing 123')
    parser.add_argument('--file', type=str, default='cat-food-ingredients.json', help='Path to cat food json file')
    args = parser.parse_args()
    return args


def read_json(file):
    '''
    Read JSON file
    :param file: Path to JSON file
    '''
    with open(file, 'r') as f:
        data = json.load(f).get('products')
    return data


def normalize_ingredients(ingredients: list[str]) -> list[str]:
    '''
    Normalize Ingredients list. This function splits the ingredients by spaces for cheap normalization, i.e. 
    chicken, Chicken Meal, Chicken By-Product Meal

    :param ingredients: List of string ingredients
    '''
    normalized_list = []
    for ingredient in ingredients:
        normalized_list.extend(ingredient.split())
    return normalized_list


def extract_allergy_ingredients(data) -> list[list[str]]:
    '''
    Extract ingredients from foods that are marked as 'Allergy'

    :param data: JSON Data
    '''
    allergens = filter(lambda x: x.get('allergy_status') == 'Allergy', data)
    allergy_foods = list(map(lambda x: x.get('name'), filter(lambda x: x.get('allergy_status') == 'Allergy', data)))
    print("Allergy foods: ", allergy_foods)
    for allergy_food in allergy_foods:
        print(allergy_food)
    allergy_food_ingredients = map(lambda x: normalize_ingredients(x.get('ingredients')), allergens)
    return list(allergy_food_ingredients)


def get_common_ingredients(sets: list[set]) -> set:
    '''
    Get common ingredients from a list of sets
    '''
    return set.intersection(*sets)


def main():
    args = parse_args()
    data = read_json(args.file)
    allergy_food_ingredients: list[list[str]] = extract_allergy_ingredients(data)
    print(get_common_ingredients(list(map(set, allergy_food_ingredients))))


if __name__ == '__main__':
    main()
