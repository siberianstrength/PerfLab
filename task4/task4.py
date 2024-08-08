import sys

def read_array(file_path: str) -> list:
    """
    Считывает все значения из файла построчно,
    добавляя их в массив.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    list
        Возвращает список со всеми значениями из файла.

    """
    try:
        array = []
        with open(file_path, 'r') as file:
            for line in file:
                array.append(int(line.rstrip()))
        return array
    except ValueError:
        print('Incorrect file contents.')
        sys.exit(1)
  
        
def min_amount_of_moves(array: list) -> int:
    """
    Принимает список со значениями,
    сортирует их, берёт медианное значение, так как она минимизирует
    сумму минимальных отклоенений.

    Parameters
    ----------
    array : list

    Returns
    -------
    int
        Сумма минимальных отклонений.

    """
    if not array:
        return 0
    
    nums = array.copy()
    nums.sort()
    
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test4.py <file_name>")
        sys.exit(1)

    try:
        file_name = sys.argv[1]
    except ValueError:
        print("Incorrect arguments.")
        sys.exit(1)
    
    nums = read_array(file_name)

    min_amount = min_amount_of_moves(nums)
    print(min_amount)