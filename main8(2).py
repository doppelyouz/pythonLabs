import requests


def get_todo(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{post_id}")
    if response.status_code in range(400, 600):
        print(f"Error: {response.status_code}")
    else:
        print(response.json())


get_todo(1)


class ToDo:
    def __init__(self, user_id, todo_id, title, completed):
        self.user_id = user_id
        self.id = todo_id
        self.title = title
        self.completed = completed


todo_item = ToDo(1, 1, "Sample ToDo", False)

new_todo = ToDo(2, 2, "New ToDo", True)


def post_todo(todo):
    data = {"userId": todo.user_id, "title": todo.title, "completed": todo.completed}
    response = requests.post("https://jsonplaceholder.typicode.com/todos", json=data)
    if response.status_code in range(400, 600):
        print(f"Error: {response.status_code}")
    else:
        print(response.json())


post_todo(new_todo)

new_todo.title = "Updated ToDo"
new_todo.completed = False


def put_todo(todo, chosen_id):
    data = {"userId": todo.user_id, "title": todo.title, "completed": todo.completed}
    response = requests.put(
        f"https://jsonplaceholder.typicode.com/todos/{chosen_id}", json=data
    )
    if response.status_code in range(400, 600):
        print(f"Error: {response.status_code}")
    else:
        print(response.json())


put_todo(new_todo, new_todo.id)

import random
import requests


def get_random_character():
    character_id = random.randint(1, 826)
    response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
    return response.json()


random_character = get_random_character()
print(random_character)

print("Keys of the JSON structure:", random_character.keys())

import json


def save_character_info(character):
    with open(f"info_character_{character['id']}.json", "w") as file:
        json.dump(character, file)


save_character_info(random_character)


def get_episode_ids(character):
    episode_urls = character["episode"]
    episode_ids = [url.split("/")[-1] for url in episode_urls]
    return episode_ids


episode_ids = get_episode_ids(random_character)

with open(f"all_episodes_with_character_{random_character['id']}.txt", "a") as file:
    for episode_id in episode_ids:
        file.write(f"https://rickandmortyapi.com/api/episode/{episode_id}\n")


def get_episode_structure():
    response = requests.get("https://rickandmortyapi.com/api/episode/1")
    return response.json()


episode_structure = get_episode_structure()
print(episode_structure)


class Episode:
    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created


from episode import Episode


def get_episode_data(episode_id):
    response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}")
    data = response.json()
    return Episode(**data)


episode_objects = [get_episode_data(e_id) for e_id in episode_ids]


class Character:
    def __init__(
        self,
        id,
        name,
        status,
        species,
        type,
        gender,
        origin,
        location,
        image,
        episode,
        url,
        created,
    ):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin  # This is a dictionary
        self.location = location  # This is a dictionary
        self.image = image
        self.episode = episode  # This is a list of episode URLs
        self.url = url
        self.created = created

    # Example method
    def print_details(self):
        print(f"Name: {self.name}, Species: {self.species}, Status: {self.status}")


from character import Character

random_character_obj = Character(**random_character)


class Character:
    def list_episodes(self):
        return [url.split("/")[-1] for url in self.episode]
