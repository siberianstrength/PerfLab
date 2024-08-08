import sys

def is_point_on_circle(x, y, h, k, r):
    """
    Принимает значения координат круга (x, y) и значения точек (h, k),
    также принимает радиус круга (r) и проверяет, принадлежит ли точка кругу,
    подставляя все значения в формулу (x - h)**2 + (y - k)**2 = r**2

    Parameters
    ----------
    x : INT
    y : INT
    h : INT
    k : INT
    r : INT

    Returns
    -------
    int
        Возвращает значение INT, где 
        0 - Точка лежит на окружности,
        1 - Точка лежит внутри окружности
        2 - Точка лежит снаружи окружности,
        -1 - Ошибка.

    """
    # Проверяем, выполняется ли уравнение окружности
    expression = (x - h)**2 + (y - k)**2
    r2 = r**2
    if expression == r2:
        return 0
    elif expression < r2:
        return 1
    elif expression > r2:
        return 2
    else:
        return -1


def read_circle_coords_file(file_path: str) -> tuple:
    """
    Принимает название файла, и считывает данные из него.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    tuple
        Возвращает кортеж, содержащий x, y, r.

    """
    try:
        with open(file_path, 'r') as file:
            x, y, r = map(int, file.read().split())
            return x, y, r
        
    except FileNotFoundError:
        print("Incorrect file name for circle's coordinates.")
        sys.exit(1)
        
    except ValueError:
        print('Incorrect file contents in points file.')
        sys.exit(1)
      
        
def read_points_file(file_path: str) -> tuple(list):
    """
    Принимает название файла и считывает данные из него, 
    добавляя в массив точек.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    tuple(list)
        Возвращает кортеж с кортежами, содержащий координаты точек внутри.
        Пример:
            ((0,0),
             (1, 1),
             (2, 2))
    """
    try:
        points = []
        with open(file_path, 'r') as file:
            for line in file:
                h, k = map(int, line.rstrip().split())
                points.append(tuple(h, k))
            return points
    except FileNotFoundError:
        print("Incorrect file name for points' coordinates.")
        sys.exit(1)
        
    except ValueError:
        print('Incorrect file contents in points file.')
        sys.exit(1)
        

def check_for_points_belonging(circle_coords: list, points: list) -> None:
    """
    Печатает координаты круга, его радиус, а также все точки и их 
    принадлежности к кругу.

    Parameters
    ----------
    circle_coords : list
    points : list

    Returns
    -------
    None

    """
    x, y, r = circle_coords
    print(f"Circle's x: {x}, y: {y}, r: {r}\n")
    for point in points:
        result = is_point_on_circle(x, y, *point, r)
        print(f'Point with x: {point[0]}, y: {point[1]}\nResult: {result}\n') 

            
        
        
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python test2.py <file_name> <file_name>")
        sys.exit(1)

    try:
        circle_coords_file = sys.argv[1]
        points_file = sys.argv[2]
    except ValueError:
        print("Incorrect arguments.")
        sys.exit(1)
        
    circle_coords = read_circle_coords_file(circle_coords_file)
    points = read_points_file(points_file)

    check_for_points_belonging(circle_coords, points)