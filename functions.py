#arbitary arguments
def marvel_function(*args): 
    # print(args)
    for hero in args:
        print(hero)
    
    print("**************")

#keyword Arguments
#arbitary keywords arguments
def dc_function(**args):
    print("Args: ", args)
    print(args['hero_1'])

dc_function(hero_1 = "Super Man", hero_2 = "Bat Man", hero_3 = "Aqua Man")

# def test_function(arg_1, arg_2):
#     print(arg_1, arg_2)


# test_function("Iron Man", "Ant Man")
    





    # marvel = ["Iron Man", "Ant Man", "Spider Man"]

    # for hero in marvel:
    #     if hero == marvelsuperhero:
    #         print("Yes, your fav hero: "+ hero + " available in Marvels!")


# def dc_function(dcsuperhero):
#     dc = ['Super Man', 'Bat Man']

#     for hero in dc:
#         if hero == dcsuperhero:
#              print("Yes, your fav hero: "+ hero + " available in DC!")


# marvel_function("Iron Man", "Ant Man", "Spider Man") # Run Time
# marvel_function("Iron Man", "Ant Man", "Spider Man", "Hulk")
# marvel_function("Iron Man", "Ant Man")

# dc_function("Super Man") # Run Time

