class Settings():

    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        #self.bg_color = (230, 230, 230)
        self.bg_color = (40, 160, 200)
        self.ship_speed = 5.5

        self.bullet_speed = 10
        self.bullet_width = 3
        #self.bullet_width = 15
        self.bullet_height = 15
        #self.bullet_height = 3
        self.bullet_color = (60, 60, 60)

        self.bullets_allowed = 8
        self.alien_speed = 2

        self.fleet_drop_speed = 34
        self.fleet_direction = 1

        self.ship_limit = 3

        self.speedup_scale = 1.25

        self.initialize_dynamic_settings()
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):

        self.ship_speed = 5.5
        self.bullet_speed = 10
        self.alien_speed = 2

        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
