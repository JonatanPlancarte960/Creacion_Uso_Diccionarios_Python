planet = {
    'name' : 'Mars',
    'moons' : 2
}

print(f'{planet.get("name")} has {planet.get("moons")} moon(s)')

planet['circumference(km)'] = {
    'polar' : 6752,
    'ecuatorial' : 6792
}
print(f'The polar circumference of {planet.get("name")} is {planet["circumference(km)"]["polar"]}')