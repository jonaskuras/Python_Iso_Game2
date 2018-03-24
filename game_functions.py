
def draw_map(map_data, height_data, screen, gs, tiles):
    # pull in the images
    floor = tiles.floor
    wall_l = tiles.wall_l
    blank = tiles.blank

    # starting x axis
    startx = 480

    # holds the current map row we are working on (y) and tile (x)
    currentRow = 0
    currentTile = 0
    for row, row_h in zip(map_data, height_data):
        for a, a_h in zip(row, row_h):  # Get individual tile image and tile height
            # x is the index of the current Tile * the tile width, a_h is from the height map
            cartx = startx + (currentTile * gs.tileWidth) - (a_h * gs.height_modifier)
            # y is the index of the currentRow * the tile height, a_h is from the height map
            carty = currentRow * gs.tileHeight - (a_h * gs.height_modifier)
            x = (cartx - carty) / 2
            y = (cartx + carty) / 4
            if a == 0:
                tileImage = blank
            elif a == 1:
                tileImage = floor
            else:
                tileImage = wall_l
            screen.blit(tileImage, (x, y))  # display the actual tile
            currentTile += 1
        currentTile = 0
        currentRow += 1
