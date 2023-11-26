import requests

def get_todo():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.status_code, response.json()

def post_todo():
    data = {"userId": 1, "id": 201, "title": "new", "completed": False}
    response = requests.post("https://jsonplaceholder.typicode.com/todos/", json=data)
    return response.status_code, response.json()

def put_todo():
    data = {"userId": 1, "id": 1, "title": "updated", "completed": True}
    response = requests.put("https://jsonplaceholder.typicode.com/todos/1", json=data)
    return response.status_code, response.json()

get_result = get_todo()
post_result = post_todo()
put_result = put_todo()

print("GET Request Result:", get_result)
print("POST Request Result:", post_result)
print("PUT Request Result:", put_result)

def get_character(character_id):
    response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
    return response.status_code, response.json()

def get_episode(episode_id):
    response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}")
    return response.status_code, response.json()

character_result = get_character(2) 
episode_result = get_episode(28)   

print("Character Request Result:", character_result)
print("Episode Request Result:", episode_result)
