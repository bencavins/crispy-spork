select_all = """
SELECT *
FROM charactercreator_character
"""

count_characters = """
SELECT count(*)
FROM charactercreator_character
"""

count_mage = """
SELECT count(*)
FROM charactercreator_mage
"""

count_items = """
SELECT count(*)
FROM armory_item
"""

count_nonweapons = """
SELECT count(*)
FROM armory_item as ai
LEFT JOIN armory_weapon as aw
		ON ai.item_id = aw.item_ptr_id
WHERE aw.item_ptr_id is NULL
"""

count_items_by_character = """
SELECT c.character_id, c.name, count(ai.item_id)
FROM charactercreator_character as c
JOIN charactercreator_character_inventory as ci
	ON c.character_id = ci.character_id 
JOIN armory_item as ai
	ON ai.item_id = ci.item_id
GROUP BY c.character_id, c.name
LIMIT 20
"""

create_character_table = """
CREATE TABLE IF NOT EXISTS charactercreator_character (
	character_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	level INT NOT NULL,
	exp INT NOT NULL,
	hp INT NOT NULL,
	strength INT NOT NULL,
	intelligence INT NOT NULL,
	dexterity INT NOT NULL,
	wisdom INT NOT NULL
)
"""

avg_weapon_count = """
SELECT AVG(item_count)
FROM
(
SELECT c.character_id, c.name, count(ai.item_id) as item_count
FROM charactercreator_character as c
JOIN charactercreator_character_inventory as ci
	ON c.character_id = ci.character_id 
JOIN armory_item as ai
	ON ai.item_id = ci.item_id
JOIN armory_weapon as aw
	ON ai.item_id = aw.item_ptr_id
GROUP BY c.character_id, c.name
)"""

create_titanic_table = """
CREATE TABLE IF NOT EXISTS titanic (
	id SERIAL PRIMARY KEY,
	survived INT NOT NULL,
	pclass INT NOT NULL,
	name VARCHAR(255) NOT NULL,
	sex VARCHAR(36) NOT NULL,
	sibs_spouses INT NOT NULL,
	parents_children INT NOT NULL,
	fare NUMERIC(5, 2) NOT NULL
)
"""