import csv
from DoubleLinkedList import DoubleLinkedList
from Country import Country
from Department import Department
from City import City

class File():
    def __init__ (self):
        pass
    
    def read_divipola(self, file_path):
        countries = DoubleLinkedList()
        colombia = Country("CO", "Colombia")
        countries.append(colombia)

        departments = {}

        with open(file_path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dept_code = row["cod_depto"]
                dept_name = row["departamento"]

                city_code = row["cod_municipio"]
                city_name = row["municipio"]

                lat = row["latitud"]
                lon = row["longitud"]
        
                if dept_code not in departments:
                    new_dept = Department(dept_code, dept_name)
                    countries.add_child(colombia, new_dept)
                    departments[dept_code] = new_dept
                    
                new_city = City(city_code, city_name, lat, lon)
                current_dept = departments[dept_code]
                countries.add_child(current_dept, new_city)
    
        return countries