namespace SpriteKind {
    export const Dialogue = SpriteKind.create()
    export const Background = SpriteKind.create()
}
namespace MapConnectionKind {
    export const Left_arrow = MapConnectionKind.create()
    export const Right_arrow = MapConnectionKind.create()
}
function initialize_game () {
    menu_selector_image = tilemap`Menu_Selector`
    map_zone_1 = tilemap`mz_1`
    map_zone_2 = tilemap`mz_2`
    current_zone = "mz_1"
    tiles.setCurrentTilemap(menu_selector_image)
    player_1 = sprites.create(assets.image`walk_1`, SpriteKind.Player)
    info.setLife(1)
    info.setScore(10)
    on_dialogue = false
    tileUtil.connectMaps(menu_selector_image, map_zone_1, MapConnectionKind.Left_arrow)
    tileUtil.connectMaps(map_zone_1, map_zone_2, MapConnectionKind.Door1)
    tiles.placeOnRandomTile(player_1, sprites.dungeon.collectibleInsignia)
    player_speed = 200
    controller.moveSprite(player_1, 100, 100)
}
sprites.onCreated(SpriteKind.Enemy, function (sprite) {
    sprite.follow(player_1, 30)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestOpen, function (sprite5, location2) {
    if (controller.A.isPressed()) {
        if (current_zone == "mz_1") {
            on_dialogue = true
            story.startCutscene(function () {
                story.spriteSayText(player_1, "Already open. . .", 1, 15, story.TextSpeed.Slow)
                story.spriteSayText(player_1, "Obviously.", 1, 15, story.TextSpeed.Slow)
                story.spriteSayText(player_1, "God forbid I find something useful.", 1, 15, story.TextSpeed.Slow)
                story.cancelAllCutscenes()
                on_dialogue = false
            })
        }
    }
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    y_direction = -200
    x_direction = 0
    animation.runImageAnimation(
    player_1,
    assets.animation`walk_up_animation`,
    200,
    true
    )
})
function initialize_menu () {
    on_menu = true
    on_help = false
    initialize_game()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (info.score() < 10) {
        info.setScore(10)
        music.play(music.melodyPlayable(music.beamUp), music.PlaybackMode.UntilDone)
    }
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite3, otherSprite) {
    sprites.destroy(sprite3, effects.spray, 500)
    sprites.destroy(bullet, effects.none, 0)
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.UntilDone)
})
scene.onOverlapTile(SpriteKind.Player, tileUtil.arrow3, function (sprite2, location) {
    tiles.placeOnRandomTile(player_1, sprites.dungeon.floorLight4)
    on_help = true
    story.startCutscene(function () {
        help_img = sprites.create(img`
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccbbbbccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffcbbcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbffffffbcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffcd1111dbfffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffccfffccfffccffffffffffffffffffffffccfffffffffffffffffffffffffffffffffffffffff
            ffffffcd11111ddcffffffdddbffffffffffffffffffffffdfffffffffffcfffcfffffffffffffffffcbffffbbffffbffffffcfffffffffffffffdcffffffffffffffffcffffffffffffffffffffffff
            fffffcb111dbddddcfffff1ccdcffffffffffffffffffffc1cfffffffffc1cfcdfffffffffffffffffbffffccbcffffcfffffdcffffffffffffffdbfffffffffffffffcdffffffffffffffffffffffff
            ffffcdd11dd11111dfffff1ffdbbbdbcdddccdbcfddbffff1bdbfcdfcdcd1dcd1bccdddfcbbdbfffffbffffbffbffffbffffb1dcfbddcffffddbfdbddcfcddbffbddccd1bfffffffffffffffffffffff
            ffffbdd11d1111111cffff1cb1cb1cfbbfdcdbffcdfffffc1bf1cc1fcdcf1cfcdffdcfdbcdcc1cffffcfffccffbffffbfffff1cfbdfbdfffcdfffddfbdf1cfdcbdfcdfcdffffffffffffffffffffffff
            ffffbdd11d1111111cffff1bbcfbdffdbbdfcdbcfddcfffc1cfdbcdfc1fc1ffcdff1ffbbcdff1cffffcfffbffffcfffbfffffdcfdbfcdffffddcfdbfbdcdcfdbbbfc1fbdffffffffffffffffffffffff
            ffffbdd11b111111dcffff1ffffcdffddcfffcdbffb1ffff1ffdcc1fc1cf1cfcdff1cfdbcdff1cffffbffcbccccdfffbfffff1cfdbfcdfffffb1cdcfcdc1cfdbbbfcdfbdffffffffffffffffffffffff
            ffffbdd11db1111dcfffff1ffffbdffbdcbfbbdbcbb1fffc1cbdcc1bddccdbccdcfbdbdccdffdcffffbffbcffffccffbfffffdbccdbdbfffcbbdcbcfbdfdbbdccdbdbfcdccdbffffffffffffffffffff
            ffffcdd111ddbdddcfffffbffffccfffbbcfcbbfcbbcffffcbbcffbbcccfcbcfbbcfbbcffcffcfffffccfbffffffbfccfffffcbcfcbcffffccbcfccfccfcbbcffcbbfffbbcccffffffffffffffffffff
            fffffbb111111111cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbffffffffffbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbffffffffbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbcffffcbcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcddddcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbbbbbcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbcfffcccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffcbddbcffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffccffffffffbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffcd11111bffffffbddbffffffffffffffffffffffcdfffffffffffffffffffffffffffffffffccfffffffffcbffffffffffffffffffffffffffbcfffffffffffffffcbffffffffffffffffffff
            fffffffd1111111bfffffdbcddfffffffffffffffffffffcdffffffffffcdffcdfffffffffffffffffbfffbbbbbfffccffffccfffffffffffffffffffdcfffffffffffffffcdffffffffffffffffffff
            fffffcb11111111dcffffdbfcdcbcdccddbfbddfcddcfffcdbdcfbcfcbcd1dbd1bfcddbfccbdbfffffcfffbfffcbfffbfffcdbcffccfffffcccffcccfdcffcccfffcccfffcbdffffffffffffffffffff
            fffffdb11bbbbbbbcffffdbcdbcddccdccdcdcffdbfffffc1ccdcdbfbbfbdffbdcfdccdcbdbcdfffffffffbfffccfffbfffbddccdbddffffdddcbbbdfdcfbdbdcfbdbdccdbbdffffffffffffffffffff
            ffffcdb11b111111dffffddbbffdbfcdcbbfbdcfbdbffffcdffdcdbfbbfcdffcdfcdcfdbcdffdfffffffffbbbbbcfffbffffdbfcdfc1cfffdbfcdccdfdcfdbfbdcdff1cbdfcdffffffffffffffffffff
            ffffc1b11b111111dffffdbffffdcfbdbcfffcdcfcdbfffcdfcdcdbfbbfcdffcdfcdcfdbcdffdcffffffffbffffbfffbffffbbfbdffdcfffdcfc1ddcfdcfdcfbdbdfcdcbbfcdffffffffffffffffffff
            ffffc1b11dd11111cffffdbffffdcfcdccccccdcbcbbfffcdcbbfbbcddfcdcfcdcfdbcdccdffdcffffcfffbffffcfffbffffdbfcdfcdcfffdbfcdcfffdcfdbfbbbdfc1cbdfbdcfcfffffffffffffffff
            ffffcdb111dddbddcffffbcffffbcffcdbccbdbfcbbffffcbbbffcbbfbffbbcfbbfcbbcfcbffbfffffbfffbccccbffccffffbdbcdddbffffdcffbdbbfbdccdbdffdbbdccdbbdcbdfffffffffffffffff
            fffffbb111111111cfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffcccccfffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffcbbbbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffffffffccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbfffffffccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbcccccbcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffbffffcbfffffffffffffffffffbfffffffffccfccfffffffffcbfffffffffffffffffffffffffffffffffffffffffffffffffccfffffffffffffffffffff
            ffffffffffffffffffffddffffffffffffffbcfffcdffffffffffffffffffcdfffffffffdbfbbfffffffffcbfffffffffffffccffffffffffffffffffffffffffffffffffbcfffffffffffffffffffff
            fffffffffffffffffffcd1cfffffcffcccffcfffccdfffffcccffffccfffcc1fffffcccfdbffffffccfccffcffffcfffcccffbdcffccffffffccffffcffffccffffcffcffcfffccfffccffffffffffff
            fffffffffffffffffffbbdbffdffdccdbdbfdcfddbdffffcdbdccddddcfbdbdffffcdbdfdbfbbfdbdddb1fcdfbbdddfcdbdbcddbfbbbbffffdbdbcdbddfcdbdcbdddddddfbcfbbbdcdbbffffffffffff
            fffffffffffffffffffdccdffdff1cdbfbdcdccdfcdffffdcfdbf1bfdccdfcdffffdccdcdbfbbfddfdbfdccdfb1cc1fdbfbbfbbfc1fcdfffcdfbbc1cc1cbdfdbc1cc1cc1fdcc1ccdc1cfffffffffffff
            ffffffffffffffffffc1dd1ccdff1cdbfcdfdcbdfcdffff1cfdbfdcfdcbdfcdffff1bdbfdcfbbfdcfdcfdccdfcdfc1c1cfbbfbbfc1ddcfffbdddccdcf1cddddfcdfc1fcdfdcc1ddcfbddffffffffffff
            ffffffffffffffffffdbccdbcdfcdfddfbdfdcbdfb1ffffdcf1bfdcfdcbdfc1ffff1ccffdbfbbfdcfdcfdccdfcdfc1f1cfddfbbfc1cfffffbdcffc1ffdcbdcffcdfc1fcdfdcc1cffffcdcfcfffffffff
            ffffffffffffffffffdcffcdcdbdbfcdbdcfdbcdbbdcfffbdbbdfdcfdccdbbdcfffbdbbfbdcbdfdcfdcfdccdccdfcdfbdbbdfcdbfdbbbfffcdbbccdffdccdbbccdfcdfcdfbdfddbbcdbdcbdfffffffff
            ffffffffffffffffffffffffffcfffffcffffcffcfffffffcfffffffffffcfffffffccfffcffcffffffffffcfffffcffccfffffcffccffffffccfffffffffccfffffcfffffcffccffccfffcfffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffcbbccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbddbfffbdddfffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffcd11111cfffffffffffffffffffffffffffffffffffccffffffffffcffffffffffffffffffffffffffffffffffddd1dbfbd1d1dffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffb1111111cfffdcffdcfffffffffffffffffffffffffdcfffffffffcdffffffffffffffffffffffffffffffcfffdd1dddcbd1d11ffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffcb111ddd1ddcffbbfbdffffffffffffffffffffffffffdcfffffffffcdffffffffffffffffffffffffffffcddcff11d11dddd11ddffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffbb11bddbbbbbffcdcdcfdddcfdcfbcffffbddcfbcddcfdcfbcfbbfffc1bdbffbbdbfbcfcbfbddbfffcdfbbbbdcff1d111d1111d11ffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffcdb11b1111d1dfffb1dfbdfc1cdcfdbfffcdfcdcddfbdfdcfdcfbbfffc1ccdcbdfbdfdbfbdcdfcdffffdbdcffdcffd11dd111dd11dffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffcdb11b111111dfffcdcfbbfc1c1cfdbfffbdfcdcbbfcbfdcfdbfbbfffcdffdcdbfcdfdbfbdcdbdbffffc1bffcdcffd1d11d1111dddffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffcdb11bd11111bffffdcfbdfcdcdcfdbfffbdfcdcbbfcdfdcfdbfdbfffcdffdcdbfbdfdbfdbcdbcfffffdbdfffdcffccddd1dd1d1bcffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffcdb111dddddbcffffdcfcdbdbfdbbdbfffcdbbbfbbfcbfdbfddbddfffcdffdcbdbddfbdbdff1bbbfffbdfdbffdcfffcddd1d1dddcfffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffbb11111d1d1cffffcfffcbcffcbcfcffffcbcffccfccfcbfcbccdffffcffcffcbccffbbcffcbccfffccfccffcffffffbd11d1bfffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffcbdddddddbffffffffffffffffffffffffffffffffffffffccbdffffffffffffffffffffffffffffffffffffffffffcbd1dbcfffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffbdbcffffffffffffffffffffffffffffffffffffffffffffd1dcffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffcccffffffffffffffffcbffffbcfffffffffffcbfffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffcdbdbfffffffffffffffcdffffdcfffffffffffbdffffcdcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffdbfffffcbbfffbbcffcbbdffffdcfccfccffbbcbdcbcfc1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffdcffffcdcdbfbbbdccdbbdffffdcfdcfbbfbdbcb1bbdfc1ffffffccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffcdcffbfbbfcdcdcfdbbdfcdffffdcfdcfbbcdcffbdfbdfcdfffffb11dcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffdcffdcdbfcdcdffdbbbfcdffffdcfdcfbbc1cffcdb1cffbffffb11dddffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbdbbbcffffffff
            ffffffffffffffffffffdbfc1cbdfbdcdcfdcbdfbdcfffdcfdbfdbcdcffbdcdcffcffffb1ddddcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbcfffcbcfffffff
            ffffffffffffffffffffcddbdccbddcfcddbffddbdcfffbdccdbcbfcddccdfbdfcdffffb1d111cfcccfccccbcffffffffffffffffffffffffffffffffffffffffffffffffffffffbcfffffffcbffffff
            ffffffffffffffffffffffccdffffffffffffffffffffffffffffffffffffffffffffffb11dddfffcffffcfcffffffffffffffffffffffffffffffffffffffffffffffffffffffccfffffffffccfffff
            fffffffffffffffffffffffbbfffffffffffffffffffffffffffffffffffffffffffffffcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffbbcbbfffccffff
            fffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbcfffbfffccffcbffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffbfffccfffdffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbffffbbbbdcfffbffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffbffffbfffdffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbffffbffffcfffbffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbfffbcccccffccffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffcccccfffbfffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffffffffbcfffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbfffffffbcffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbcccccbcfffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccffffffcffffffffcffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbcffffffbfffffffcbfffccfffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccffbcbffbccbccbccbbcfbbccbffdcbbcbbbbbcbcbff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccbbfbffbcbbcbbfcbdffccbcbffbcbcbdbcbcbdcbff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbdbcbcffbbfbbbcbcbbcfcdcdbffbccccbbcbccbdbff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccfffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            `, SpriteKind.Background)
        tiles.placeOnRandomTile(help_img, sprites.dungeon.floorLight4)
        pause(5000)
        story.cancelAllCutscenes()
        on_help = false
    })
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (info.score() > 0) {
        bullet = sprites.createProjectileFromSprite(img`
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
            `, player_1, x_direction, y_direction)
        info.changeScoreBy(-1)
        music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
    } else {
        music.play(music.melodyPlayable(music.bigCrash), music.PlaybackMode.UntilDone)
    }
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`walk_down_1`)
})
scene.onOverlapTile(SpriteKind.Player, tileUtil.door0, function (sprite22, location3) {
    tileUtil.loadConnectedMap(MapConnectionKind.Door1)
    tiles.placeOnRandomTile(player_1, tileUtil.door0)
    if (tileUtil.currentTilemap() == map_zone_2) {
        info.startCountdown(300)
        player_1.x = 26
    } else {
        player_1.x = 231
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    y_direction = 0
    x_direction = -200
    animation.runImageAnimation(
    player_1,
    assets.animation`WalkLeft`,
    200,
    true
    )
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`walk_right_1`)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`walk_left_1`)
})
info.onCountdownEnd(function () {
    music.stopAllSounds()
    game.setGameOverMessage(true, "YOU SURVIVED")
    game.setGameOverEffect(true, effects.slash)
    game.gameOver(true)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    y_direction = 0
    x_direction = 200
    animation.runImageAnimation(
    player_1,
    assets.animation`WalkRight`,
    200,
    true
    )
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`walk_up_1`)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    y_direction = 200
    x_direction = 0
    animation.runImageAnimation(
    player_1,
    assets.animation`walk_down_animation`,
    200,
    true
    )
})
info.onLifeZero(function () {
    music.stopAllSounds()
    game.setGameOverMessage(false, "YOU GOT CAUGHT!")
    game.setGameOverEffect(true, effects.dissolve)
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, tileUtil.arrow4, function (sprite23, location4) {
    on_menu = false
    tileUtil.loadConnectedMap(MapConnectionKind.Left_arrow)
    tiles.placeOnRandomTile(player_1, sprites.dungeon.collectibleInsignia)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite4, otherSprite2) {
    info.setLife(0)
})
tileUtil.onMapLoaded(function (tilemap2) {
    if (tileUtil.currentTilemap() == map_zone_1) {
        tileUtil.coverAllTiles(tileUtil.door0, sprites.dungeon.doorOpenEast)
    } else if (tileUtil.currentTilemap() == map_zone_2) {
        tileUtil.replaceAllTiles(tileUtil.door0, sprites.builtin.forestTiles10)
    } else {
    	
    }
})
let help_img: Sprite = null
let bullet: Sprite = null
let on_help = false
let on_menu = false
let x_direction = 0
let y_direction = 0
let player_speed = 0
let on_dialogue = false
let player_1: Sprite = null
let current_zone = ""
let map_zone_2: tiles.TileMapData = null
let map_zone_1: tiles.TileMapData = null
let menu_selector_image: tiles.TileMapData = null
initialize_menu()
game.onUpdate(function () {
    if (on_dialogue) {
        controller.moveSprite(player_1, 0, 0)
        animation.stopAnimation(animation.AnimationTypes.All, player_1)
    } else {
        controller.moveSprite(player_1, 100, 100)
    }
    if (on_help) {
        controller.moveSprite(player_1, 0, 0)
        animation.stopAnimation(animation.AnimationTypes.All, player_1)
    } else {
        sprites.destroy(help_img)
    }
})
game.onUpdateInterval(5000, function () {
    tileUtil.createSpritesOnTiles(sprites.dungeon.collectibleRedCrystal, assets.image`Ghost`, SpriteKind.Enemy)
    tileUtil.createSpritesOnTiles(sprites.dungeon.collectibleBlueCrystal, assets.image`Ghost`, SpriteKind.Enemy)
})
forever(function () {
    scene.centerCameraAt(0, 0)
    scene.cameraFollowSprite(player_1)
    if (on_menu == false) {
        music.play(music.stringPlayable("C5 A B G A F G E ", 147), music.PlaybackMode.UntilDone)
    }
})
