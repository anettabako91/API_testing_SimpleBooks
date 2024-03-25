import requests


def get_status():  # fara parametru
    return requests.get("https://simple-books-api.glitch.me/status")


# apelam metoda/functia altfel la run nu va aparea nimic
# trebuie neaparat cu print altfel nu vom vedea nimic
# .json ca sa vedem exact body-ul ce am vazut in postman
# .status_code ne returneaza status code-ul requestului trimis
#
# print(get_status().json())
# print(get_status().status_code)

# metoda sau functie -> functia este cea cu def , metoda cand cream clasa si in interiorul clasei definim metoda
# metoda traieste in interiorul unei clase , poate fi apelata doar cand clasa este instantiata ( Status().get_status().)
