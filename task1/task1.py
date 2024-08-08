import sys

def circular_array_path(n, m):
    """
    Создать круговой массив и вывести его путь

    Parameters
    ----------
    n : INT
    m : INT

    Returns
    -------
    STR
        Возвращает путь в виде строки.

    """
    # Круговой массив задаётся лишь от 1:n+1 
    # т.к. это позволит не убить программу в случае, если n очень велико
    # (i.e. n = 10e20).
    array = [i for i in range(1, n + 1)]
    result_path = [array[0]]
    
    idx = 0
    # Добавление элемента по индексу.
    # Предусмотрен кейс, когда m > n.
    while True:
        idx = (idx + m - 1) % n
        if array[idx] == array[0]:
            break
        result_path.append(array[idx])
    
    return ''.join(map(str, result_path)) 


if __name__ == "__main__":
    # Проверки на корректность введённых значений.
    if len(sys.argv) != 3:
        print("Usage: python test1.py <x> <y>.")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be integers.")
        sys.exit(1)

    if n <= 0 or m <= 0:
        print("Both arguments must be positive integers.")
        sys.exit(1)

    print(circular_array_path(n, m))