# import pygame 
# pygame.init()
# windowSize=(800,500)
# screen=pygame.display.set_mode(windowSize)
# image=pygame.image.load('graphics/ground.png')
# x=50
# y=50
# finished=False
# while not finished:
#     screen.fill('white')
#     keys=pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         y-=1
#     if keys[pygame.K_s]:
#         y+=1   
#     if keys[pygame.K_a]:
#         x-=1
#     if keys[pygame.K_d]:
#         x+=1
   
# newImage=pygame.transform.scale(image,(x,y))
# screen.blit((newImage,20,20))
# pygame.display.flip()
# for event in pygame.event.get():
#     if event.type==pygame.QUIT:
#         finished=True
# pygame.quit()
