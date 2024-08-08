import json
import sys

def read_json_file(file_path: json) -> dict:
    """
    Считывает данные из json файла.

    Parameters
    ----------
    file_path : json

    Returns
    -------
    dict
        Возвращает словарь с данными из json файла.

    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except:
        print('Incorrect file path.')
        sys.exit(1)


def write_json_file(file_path: str, data: dict) -> None:
    """
    Принимает путь к файлу, а также изменённые данные и записывает
    их в новый json файл.

    Parameters
    ----------
    file_path : str
    data : dict

    Returns
    -------
    None
        DESCRIPTION.

    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print('Success')
    except Exception as e:
        print(f'{e}: data dump has failed')
        

def update_values(data: list, values_to_insert: dict) -> dict:
    """
    Принимает list и dict, запускает изменение данных.

    Parameters
    ----------
    data : list
    values_to_insert : dict

    Returns
    -------
    dict
        Словарь с изменёнными данными.

    """
    
    # Создаём массив для быстрого поиска
    value_dict = {item['id']: item['value'] for item in values_to_insert['values']}
    
    def recursive_update(item: list) -> None:
        """
        Рекурсивно обходит значения, сопоставляя их с нужными значениями
        из value_dict.

        Parameters
        ----------
        item : list

        Returns
        -------
        None.

        """
        # Если у элемента есть id и если id в value_dict 
        if 'id' in item and item['id'] in value_dict:
            item['value'] = value_dict[item['id']]
        
        # Рекурсивно обходим вложенные значения
        if 'values' in item and isinstance(item['values'], list):
            for sub_item in item['values']:
                recursive_update(sub_item)
    
    for entry in data:
        recursive_update(entry)
    
    return data

            
        
        
    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python test3.py <file_name> <file_name> <file_name>")
        sys.exit(1)

    try:
        file_name_tests = sys.argv[1]
        file_name_values = sys.argv[2]
        output_file_name = sys.argv[3]
        
    except ValueError:
        print("Incorrect arguments.")
        sys.exit(1)
        
    tests_data = read_json_file(file_name_tests)['tests']

    insertion_values = read_json_file(file_name_values)
    
    updated_data = update_values(tests_data, insertion_values)
    
    write_json_file(output_file_name, updated_data)