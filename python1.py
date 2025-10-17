def is_leap_year(year: int) -> bool:
    """
    Функція перевіряє, чи є рік високосним.
    
    Args:
        year (int): Рік для перевірки
        
    Returns:
        bool: True якщо рік високосний, False якщо ні
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def main():
    """
    Основна функція програми для введення років та перевірки на високосність.
    """
    print("Програма для перевірки високосних років")
    print("Введіть рік для перевірки (0 для виходу):")
    
    while True:
        try:
            
            user_input = input("Введіть рік: ").strip()
            
            
            if user_input == "0":
                print("Вихід з програми...")
                break
              
            year = int(user_input)
            
            if is_leap_year(year):
                print(f"Рік {year} - ВИСОКОСНИЙ")
            else:
                print(f"Рік {year} - не високосний")
                
            print()  
            
        except ValueError:
            print("Помилка: Будь ласка, введіть ціле число!")
            print()

if __name__ == "__main__":
    main()
