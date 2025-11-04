@namespace
class SpriteKind:
    Dialogue = SpriteKind.create()
    Background = SpriteKind.create()
@namespace
class MapConnectionKind:
    Left_arrow = MapConnectionKind.create()
    Right_arrow = MapConnectionKind.create()
def initialize_game():
    global menu_selector_image, map_zone_1, map_zone_2, current_zone, player_1, on_dialogue, player_speed
    menu_selector_image = tilemap("""
        Menu_Selector
        """)
    map_zone_1 = tilemap("""
        mz_1
        """)
    map_zone_2 = tilemap("""
        mz_2
        """)
    current_zone = "mz_1"
    tiles.set_current_tilemap(menu_selector_image)
    player_1 = sprites.create(assets.image("""
        walk_1
        """), SpriteKind.player)
    info.set_life(1)
    info.set_score(10)
    on_dialogue = False
    tileUtil.connect_maps(menu_selector_image,
        map_zone_1,
        MapConnectionKind.Left_arrow)
    tileUtil.connect_maps(map_zone_1, map_zone_2, MapConnectionKind.door1)
    tiles.place_on_random_tile(player_1, sprites.dungeon.collectible_insignia)
    player_speed = 200
    controller.move_sprite(player_1, 100, 100)

def on_on_created(sprite):
    sprite.follow(player_1, 30)
sprites.on_created(SpriteKind.enemy, on_on_created)

def on_overlap_tile(sprite5, location2):
    global on_dialogue
    if controller.A.is_pressed():
        if current_zone == "mz_1":
            on_dialogue = True
            
            def on_start_cutscene():
                global on_dialogue
                story.sprite_say_text(player_1, "Already open. . .", 1, 15, story.TextSpeed.SLOW)
                story.sprite_say_text(player_1, "Obviously.", 1, 15, story.TextSpeed.SLOW)
                story.sprite_say_text(player_1,
                    "God forbid I find something useful.",
                    1,
                    15,
                    story.TextSpeed.SLOW)
                story.cancel_all_cutscenes()
                on_dialogue = False
            story.start_cutscene(on_start_cutscene)
            
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile)

def on_up_pressed():
    global y_direction, x_direction
    y_direction = -200
    x_direction = 0
    animation.run_image_animation(player_1,
        assets.animation("""
            walk_up_animation
            """),
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def initialize_menu():
    global on_menu
    on_menu = True
    initialize_game()

def on_b_pressed():
    if info.score() < 10:
        info.set_score(10)
        music.play(music.melody_playable(music.beam_up),
            music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap(sprite3, otherSprite):
    sprites.destroy(sprite3, effects.spray, 500)
    sprites.destroy(bullet, effects.none, 0)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_overlap_tile2(sprite2, location):
    global help_img
    help_img = sprites.create(img("""
    f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c b b b b c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f c b b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b f f f f f f b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f c d 1 1 1 1 d b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f f c c f f f c c f f f f f f f f f f f f f f f f f f f f f f c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f c d 1 1 1 1 1 d d c f f f f f f d d d b f f f f f f f f f f f f f f f f f f f f f f d f f f f f f f f f f f c f f f c f f f f f f f f f f f f f f f f f c b f f f f b b f f f f b f f f f f f c f f f f f f f f f f f f f f f d c f f f f f f f f f f f f f f f f c f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f c b 1 1 1 d b d d d d c f f f f f 1 c c d c f f f f f f f f f f f f f f f f f f f f c 1 c f f f f f f f f f c 1 c f c d f f f f f f f f f f f f f f f f f b f f f f c c b c f f f f c f f f f f d c f f f f f f f f f f f f f f d b f f f f f f f f f f f f f f f c d f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f c d d 1 1 d d 1 1 1 1 1 d f f f f f 1 f f d b b b d b c d d d c c d b c f d d b f f f f 1 b d b f c d f c d c d 1 d c d 1 b c c d d d f c b b d b f f f f f b f f f f b f f b f f f f b f f f f b 1 d c f b d d c f f f f d d b f d b d d c f c d d b f f b d d c c d 1 b f f f f f f f f f f f f f f f f f f f f f f f
        f f f f b d d 1 1 d 1 1 1 1 1 1 1 c f f f f 1 c b 1 c b 1 c f b b f d c d b f f c d f f f f f c 1 b f 1 c c 1 f c d c f 1 c f c d f f d c f d b c d c c 1 c f f f f c f f f c c f f b f f f f b f f f f f 1 c f b d f b d f f f c d f f f d d f b d f 1 c f d c b d f c d f c d f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f b d d 1 1 d 1 1 1 1 1 1 1 c f f f f 1 b b c f b d f f d b b d f c d b c f d d c f f f c 1 c f d b c d f c 1 f c 1 f f c d f f 1 f f b b c d f f 1 c f f f f c f f f b f f f f c f f f b f f f f f d c f d b f c d f f f f d d c f d b f b d c d c f d b b b f c 1 f b d f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f b d d 1 1 b 1 1 1 1 1 1 d c f f f f 1 f f f f c d f f d d c f f f c d b f f b 1 f f f f 1 f f d c c 1 f c 1 c f 1 c f c d f f 1 c f d b c d f f 1 c f f f f b f f c b c c c c d f f f b f f f f f 1 c f d b f c d f f f f f b 1 c d c f c d c 1 c f d b b b f c d f b d f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f b d d 1 1 d b 1 1 1 1 d c f f f f f 1 f f f f b d f f b d c b f b b d b c b b 1 f f f c 1 c b d c c 1 b d d c c d b c c d c f b d b d c c d f f d c f f f f b f f b c f f f f c c f f b f f f f f d b c c d b d b f f f c b b d c b c f b d f d b b d c c d b d b f c d c c d b f f f f f f f f f f f f f f f f f f f f
        f f f f c d d 1 1 1 d d b d d d c f f f f f b f f f f c c f f f b b c f c b b f c b b c f f f f c b b c f f b b c c c f c b c f b b c f b b c f f c f f c f f f f f c c f b f f f f f f b f c c f f f f f c b c f c b c f f f f c c b c f c c f c c f c b b c f f c b b f f f b b c c c f f f f f f f f f f f f f f f f f f f f
        f f f f f b b 1 1 1 1 1 1 1 1 1 c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f f f f f f f f b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f c c c c c c c c c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b f f f f f f f f b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b c f f f f c b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c d d d d c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b b b b b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b c f f f c c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f c b d d b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f f f f f f f b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f c d 1 1 1 1 1 b f f f f f f b d d b f f f f f f f f f f f f f f f f f f f f f f c d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f f f f f f f f c b f f f f f f f f f f f f f f f f f f f f f f f f f f b c f f f f f f f f f f f f f f f c b f f f f f f f f f f f f f f f f f f f f
        f f f f f f f d 1 1 1 1 1 1 1 b f f f f f d b c d d f f f f f f f f f f f f f f f f f f f f f c d f f f f f f f f f f c d f f c d f f f f f f f f f f f f f f f f f b f f f b b b b b f f f c c f f f f c c f f f f f f f f f f f f f f f f f f f d c f f f f f f f f f f f f f f f c d f f f f f f f f f f f f f f f f f f f f
        f f f f f c b 1 1 1 1 1 1 1 1 d c f f f f d b f c d c b c d c c d d b f b d d f c d d c f f f c d b d c f b c f c b c d 1 d b d 1 b f c d d b f c c b d b f f f f f c f f f b f f f c b f f f b f f f c d b c f f c c f f f f f c c c f f c c c f d c f f c c c f f f c c c f f f c b d f f f f f f f f f f f f f f f f f f f f
        f f f f f d b 1 1 b b b b b b b c f f f f d b c d b c d d c c d c c d c d c f f d b f f f f f c 1 c c d c d b f b b f b d f f b d c f d c c d c b d b c d f f f f f f f f f b f f f c c f f f b f f f b d d c c d b d d f f f f d d d c b b b d f d c f b d b d c f b d b d c c d b b d f f f f f f f f f f f f f f f f f f f f
        f f f f c d b 1 1 b 1 1 1 1 1 1 d f f f f d d b b f f d b f c d c b b f b d c f b d b f f f f c d f f d c d b f b b f c d f f c d f c d c f d b c d f f d f f f f f f f f f b b b b b c f f f b f f f f d b f c d f c 1 c f f f d b f c d c c d f d c f d b f b d c d f f 1 c b d f c d f f f f f f f f f f f f f f f f f f f f
        f f f f c 1 b 1 1 b 1 1 1 1 1 1 d f f f f d b f f f f d c f b d b c f f f c d c f c d b f f f c d f c d c d b f b b f c d f f c d f c d c f d b c d f f d c f f f f f f f f b f f f f b f f f b f f f f b b f b d f f d c f f f d c f c 1 d d c f d c f d c f b d b d f c d c b b f c d f f f f f f f f f f f f f f f f f f f f
        f f f f c 1 b 1 1 d d 1 1 1 1 1 c f f f f d b f f f f d c f c d c c c c c c d c b c b b f f f c d c b b f b b c d d f c d c f c d c f d b c d c c d f f d c f f f f c f f f b f f f f c f f f b f f f f d b f c d f c d c f f f d b f c d c f f f d c f d b f b b b d f c 1 c b d f b d c f c f f f f f f f f f f f f f f f f f
        f f f f c d b 1 1 1 d d d b d d c f f f f b c f f f f b c f f c d b c c b d b f c b b f f f f c b b b f f c b b f b f f b b c f b b f c b b c f c b f f b f f f f f b f f f b c c c c b f f c c f f f f b d b c d d d b f f f f d c f f b d b b f b d c c d b d f f d b b d c c d b b d c b d f f f f f f f f f f f f f f f f f
        f f f f f b b 1 1 1 1 1 1 1 1 1 c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f c c c c c f f f c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f c b b b b b b b b b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f f f f f f f c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b f f f f f f f c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b c c c c c b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f f c b f f f f f f f f f f f f f f f f f f f b f f f f f f f f f c c f c c f f f f f f f f f c b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f d d f f f f f f f f f f f f f f b c f f f c d f f f f f f f f f f f f f f f f f f c d f f f f f f f f f d b f b b f f f f f f f f f c b f f f f f f f f f f f f f c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b c f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f c d 1 c f f f f f c f f c c c f f c f f f c c d f f f f f c c c f f f f c c f f f c c 1 f f f f f c c c f d b f f f f f f c c f c c f f c f f f f c f f f c c c f f b d c f f c c f f f f f f c c f f f f c f f f f c c f f f f c f f c f f c f f f c c f f f c c f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f b b d b f f d f f d c c d b d b f d c f d d b d f f f f c d b d c c d d d d c f b d b d f f f f c d b d f d b f b b f d b d d d b 1 f c d f b b d d d f c d b d b c d d b f b b b b f f f f d b d b c d b d d f c d b d c b d d d d d d d f b c f b b b d c d b b f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f d c c d f f d f f 1 c d b f b d c d c c d f c d f f f f d c f d b f 1 b f d c c d f c d f f f f d c c d c d b f b b f d d f d b f d c c d f b 1 c c 1 f d b f b b f b b f c 1 f c d f f f c d f b b c 1 c c 1 c b d f d b c 1 c c 1 c c 1 f d c c 1 c c d c 1 c f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f c 1 d d 1 c c d f f 1 c d b f c d f d c b d f c d f f f f 1 c f d b f d c f d c b d f c d f f f f 1 b d b f d c f b b f d c f d c f d c c d f c d f c 1 c 1 c f b b f b b f c 1 d d c f f f b d d d c c d c f 1 c d d d d f c d f c 1 f c d f d c c 1 d d c f b d d f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f d b c c d b c d f c d f d d f b d f d c b d f b 1 f f f f d c f 1 b f d c f d c b d f c 1 f f f f 1 c c f f d b f b b f d c f d c f d c c d f c d f c 1 f 1 c f d d f b b f c 1 c f f f f f b d c f f c 1 f f d c b d c f f c d f c 1 f c d f d c c 1 c f f f f c d c f c f f f f f f f f f
        f f f f f f f f f f f f f f f f f f d c f f c d c d b d b f c d b d c f d b c d b b d c f f f b d b b d f d c f d c c d b b d c f f f b d b b f b d c b d f d c f d c f d c c d c c d f c d f b d b b d f c d b f d b b b f f f c d b b c c d f f d c c d b b c c d f c d f c d f b d f d d b b c d b d c b d f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f c f f f f f c f f f f c f f c f f f f f f f c f f f f f f f f f f f c f f f f f f f c c f f f c f f c f f f f f f f f f f c f f f f f c f f c c f f f f f c f f c c f f f f f f c c f f f f f f f f f c c f f f f f c f f f f f c f f c c f f c c f f f c f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f c b b c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b d d b f f f b d d d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f c d 1 1 1 1 1 c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f f f f f f f f f c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f d d d 1 d b f b d 1 d 1 d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f b 1 1 1 1 1 1 1 c f f f d c f f d c f f f f f f f f f f f f f f f f f f f f f f f f f d c f f f f f f f f f c d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c f f f d d 1 d d d c b d 1 d 1 1 f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f c b 1 1 1 d d d 1 d d c f f b b f b d f f f f f f f f f f f f f f f f f f f f f f f f f f d c f f f f f f f f f c d f f f f f f f f f f f f f f f f f f f f f f f f f f f f c d d c f f 1 1 d 1 1 d d d d 1 1 d d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f b b 1 1 b d d b b b b b f f c d c d c f d d d c f d c f b c f f f f b d d c f b c d d c f d c f b c f b b f f f c 1 b d b f f b b d b f b c f c b f b d d b f f f c d f b b b b d c f f 1 d 1 1 1 d 1 1 1 1 d 1 1 f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f c d b 1 1 b 1 1 1 1 d 1 d f f f b 1 d f b d f c 1 c d c f d b f f f c d f c d c d d f b d f d c f d c f b b f f f c 1 c c d c b d f b d f d b f b d c d f c d f f f f d b d c f f d c f f d 1 1 d d 1 1 1 d d 1 1 d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f c d b 1 1 b 1 1 1 1 1 1 d f f f c d c f b b f c 1 c 1 c f d b f f f b d f c d c b b f c b f d c f d b f b b f f f c d f f d c d b f c d f d b f b d c d b d b f f f f c 1 b f f c d c f f d 1 d 1 1 d 1 1 1 1 d d d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f c d b 1 1 b d 1 1 1 1 1 b f f f f d c f b d f c d c d c f d b f f f b d f c d c b b f c d f d c f d b f d b f f f c d f f d c d b f b d f d b f d b c d b c f f f f f d b d f f f d c f f c c d d d 1 d d 1 d 1 b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f c d b 1 1 1 d d d d d b c f f f f d c f c d b d b f d b b d b f f f c d b b b f b b f c b f d b f d d b d d f f f c d f f d c b d b d d f b d b d f f 1 b b b f f f b d f d b f f d c f f f c d d d 1 d 1 d d d c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f b b 1 1 1 1 1 d 1 d 1 c f f f f c f f f c b c f f c b c f c f f f f c b c f f c c f c c f c b f c b c c d f f f f c f f c f f c b c c f f b b c f f c b c c f f f c c f c c f f c f f f f f f b d 1 1 d 1 b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f c b d d d d d d d b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c b d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b d 1 d b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b d b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f d 1 d c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f c c c f f f f f f f f f f f f f f f f c b f f f f b c f f f f f f f f f f f c b f f f f f c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f c d b d b f f f f f f f f f f f f f f f c d f f f f d c f f f f f f f f f f f b d f f f f c d c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f d b f f f f f c b b f f f b b c f f c b b d f f f f d c f c c f c c f f b b c b d c b c f c 1 f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f d c f f f f c d c d b f b b b d c c d b b d f f f f d c f d c f b b f b d b c b 1 b b d f c 1 f f f f f f c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f c d c f f b f b b f c d c d c f d b b d f c d f f f f d c f d c f b b c d c f f b d f b d f c d f f f f f b 1 1 d c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f d c f f d c d b f c d c d f f d b b b f c d f f f f d c f d c f b b c 1 c f f c d b 1 c f f b f f f f b 1 1 d d d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b d b b b c f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f d b f c 1 c b d f b d c d c f d c b d f b d c f f f d c f d b f d b c d c f f b d c d c f f c f f f f b 1 d d d d c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b c f f f c b c f f f f f f f
        f f f f f f f f f f f f f f f f f f f f c d d b d c c b d d c f c d d b f f d d b d c f f f b d c c d b c b f c d d c c d f b d f c d f f f f b 1 d 1 1 1 c f c c c f c c c c b c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b c f f f f f f f c b f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f c c d f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b 1 1 d d d f f f c f f f f c f c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f f f f f f f f c c f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f b b f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c c c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f b b c b b f f f c c f f f f
        f f f f f f f f f f f f f f f f f f f f f f f c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b c f f f b f f f c c f f c b f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f d f f f f b f f f c c f f f d f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f f b b b b d c f f f b f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f d f f f f b f f f f b f f f d f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f f b f f f f c f f f b f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b f f f b c c c c c f f c c f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f c c c c c f f f b f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b f f f f f f f f f b c f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b f f f f f f f b c f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c b c c c c c b c f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f f f f f c f f f f f f f f c f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b c f f f f f f b f f f f f f f c b f f f c c f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f b c b f f b c c b c c b c c b b c f b b c c b f f d c b b c b b b b b c b c b f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c c b b f b f f b c b b c b b f c b d f f c c b c b f f b c b c b d b c b c b d c b f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f b d b c b c f f b b f b b b c b c b b c f c d c d b f f b c c c c b b c b c c b d b f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f c c f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
        f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f
            """),
        SpriteKind.Background)
scene.on_overlap_tile(SpriteKind.player, tileUtil.arrow3, on_overlap_tile2)

def on_a_pressed():
    global bullet
    if info.score() > 0:
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . 4 4 . . . . . . .
                . . . . . . 4 5 5 4 . . . . . .
                . . . . . . 2 5 5 2 . . . . . .
                . . . . . . . 2 2 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            player_1,
            x_direction,
            y_direction)
        info.change_score_by(-1)
        music.play(music.melody_playable(music.pew_pew),
            music.PlaybackMode.UNTIL_DONE)
    else:
        music.play(music.melody_playable(music.big_crash),
            music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_down_1
        """))
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_overlap_tile3(sprite22, location3):
    tileUtil.load_connected_map(MapConnectionKind.door1)
    tiles.place_on_random_tile(player_1, tileUtil.door0)
    if tileUtil.current_tilemap() == map_zone_2:
        info.start_countdown(300)
        player_1.x = 26
    else:
        player_1.x = 231
scene.on_overlap_tile(SpriteKind.player, tileUtil.door0, on_overlap_tile3)

def on_left_pressed():
    global y_direction, x_direction
    y_direction = 0
    x_direction = -200
    animation.run_image_animation(player_1,
        assets.animation("""
            WalkLeft
            """),
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_right_1
        """))
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_left_1
        """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_countdown_end():
    game.game_over(True)
    game.set_game_over_effect(True, effects.slash)
    game.set_game_over_message(True, "YOU SURVIVED")
    music.stop_all_sounds()
info.on_countdown_end(on_countdown_end)

def on_right_pressed():
    global y_direction, x_direction
    y_direction = 0
    x_direction = 200
    animation.run_image_animation(player_1,
        assets.animation("""
            WalkRight
            """),
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_up_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_up_1
        """))
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    global y_direction, x_direction
    y_direction = 200
    x_direction = 0
    animation.run_image_animation(player_1,
        assets.animation("""
            walk_down_animation
            """),
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    music.stop_all_sounds()
    game.game_over(False)
    music.play(music.string_playable("G F G A - F E D ", 120),
        music.PlaybackMode.UNTIL_DONE)
    game.set_game_over_message(False, "YOU GOT CAUGHT!")
info.on_life_zero(on_life_zero)

def on_overlap_tile4(sprite23, location4):
    global on_menu
    on_menu = False
    tileUtil.load_connected_map(MapConnectionKind.Left_arrow)
    tiles.place_on_random_tile(player_1, sprites.dungeon.collectible_insignia)
scene.on_overlap_tile(SpriteKind.player, tileUtil.arrow4, on_overlap_tile4)

def on_on_overlap2(sprite4, otherSprite2):
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_map_loaded(tilemap2):
    if tileUtil.current_tilemap() == map_zone_1:
        tileUtil.cover_all_tiles(tileUtil.door0, sprites.dungeon.door_open_east)
    elif tileUtil.current_tilemap() == map_zone_2:
        tileUtil.replace_all_tiles(tileUtil.door0, sprites.builtin.forest_tiles10)
    else:
        pass
tileUtil.on_map_loaded(on_map_loaded)

help_img: Sprite = None
bullet: Sprite = None
on_menu = False
x_direction = 0
y_direction = 0
player_speed = 0
on_dialogue = False
player_1: Sprite = None
current_zone = ""
map_zone_2: tiles.TileMapData = None
map_zone_1: tiles.TileMapData = None
menu_selector_image: tiles.TileMapData = None
initialize_menu()

def on_on_update():
    if on_dialogue:
        controller.move_sprite(player_1, 0, 0)
        animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    else:
        controller.move_sprite(player_1, 100, 100)
game.on_update(on_on_update)

def on_update_interval():
    tileUtil.create_sprites_on_tiles(sprites.dungeon.collectible_red_crystal,
        assets.image("""
            Ghost
            """),
        SpriteKind.enemy)
    tileUtil.create_sprites_on_tiles(sprites.dungeon.collectible_blue_crystal,
        assets.image("""
            Ghost
            """),
        SpriteKind.enemy)
game.on_update_interval(5000, on_update_interval)

def on_forever():
    scene.center_camera_at(0, 0)
    scene.camera_follow_sprite(player_1)
    if on_menu == False:
        music.play(music.string_playable("C5 A B G A F G E ", 147),
            music.PlaybackMode.UNTIL_DONE)
forever(on_forever)
