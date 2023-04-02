from seeds.DbSeeder import seedDatabase
import sys
import os

def migrate():
    print("migrate")
    os.system('alembic upgrade head')
    

def reset():
    print("Begin reset")
    os.system('alembic downgrade base')
    migrate()
    print("End reset")

def refresh():
    print("Begin refresh ")
    reset()
    migrate()
    dbSeed()
    print("End refresh ")
    

def dbSeed():
    print("seed")
    seedDatabase()

def main(arguments):
    if (len(arguments) == 1): 
        print("argument manquant")
        return 

    if arguments[1] == "--migrate":
        migrate()
    elif arguments[1] == "--reset":
        reset();
    elif arguments[1] == "--refresh":
        refresh()
    elif arguments[1] == "--seed":
        dbSeed()
    

# Using the special variable
# __name__
if __name__=="__main__":
    main(sys.argv)