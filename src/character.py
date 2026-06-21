class Character:
    def __init__(self, name, base_name, star, range_, hp, attack, armor, magic_resist, attack_speed, mana_initial, mana_max):
        self.name = name
        self.base_name = base_name
        self.star = star

        self.max_hp = hp
        self.hp = hp

        self.range = range_
        self.position = (0, 0)

        self.attack = attack
        self.armor = armor
        self.magic_resist = magic_resist
        self.attack_speed = attack_speed

        self.mana = mana_initial
        self.mana_initial = mana_initial
        self.mana_max = mana_max

        self.target = None
        self.attack_cooldown = 0
        self.next_attack_time = 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def heal(self, amount):
        if not self.is_alive():
            return
        self.hp = min(self.max_hp, self.hp + amount)

    def reset(self):
        self.hp = self.max_hp
        self.mana = self.mana_initial
        self.target = None
        self.next_attack_time = 0
    
    def is_alive(self):
        return self.hp > 0