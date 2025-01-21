import os
import ipaddress

def process_input_directory(input_dir, output_file):
    try:
        # Получаем список всех файлов в директории, исключая .gitkeep
        files = sorted(
            [f for f in os.listdir(input_dir) if f != ".gitkeep" and os.path.isfile(os.path.join(input_dir, f))]
        )

        # Выходной список для одиночных IP-адресов
        all_ips = set()

        for file in files:
            input_path = os.path.join(input_dir, file)

            with open(input_path, "r") as f:
                lines = f.readlines()

            for line in lines:
                line = line.strip()

                # Если это одиночный IP-адрес
                if is_valid_ip(line):
                    all_ips.add(line)

                # Если это диапазон IP-адресов
                elif "-" in line:
                    start_ip, end_ip = line.split("-")
                    if is_valid_ip(start_ip) and is_valid_ip(end_ip):
                        for ip in ip_range(start_ip, end_ip):
                            all_ips.add(ip)

                # Если это IP с маской
                elif "/" in line:
                    try:
                        network = ipaddress.ip_network(line, strict=False)
                        for ip in network.hosts():
                            all_ips.add(str(ip))
                    except ValueError:
                        pass  # Игнорируем некорректные данные

        # Запись результатов в выходной файл
        with open(output_file, "w") as f:
            for ip in sorted(all_ips, key=ip_to_sort_key):
                f.write(f"{ip}\n")

        print(f"Обработка завершена. Результат сохранен в {output_file}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ip_range(start_ip, end_ip):
    start = int(ipaddress.ip_address(start_ip))
    end = int(ipaddress.ip_address(end_ip))
    return [str(ipaddress.ip_address(ip)) for ip in range(start, end + 1)]

def ip_to_sort_key(ip):
    return tuple(map(int, ip.split(".")))

if __name__ == "__main__":
    # Директории input и output
    input_directory = "input"
    output_directory = "output"

    # Проверяем существование директорий
    if not os.path.exists(input_directory):
        os.makedirs(input_directory)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Имя выходного файла
    output_file_path = os.path.join(output_directory, "output.txt")

    # Обрабатываем директорию input и создаем файл output
    process_input_directory(input_directory, output_file_path)
