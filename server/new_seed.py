from config import app
# from models import db, User, Closet, ClothingItem
from new_models import db, User, ClothingItem, Closet
from faker import Faker
import random 

if __name__ == "__main__":
    fake = Faker()

    with app.app_context():

    # print("starting seed...")
        
        print("deleting old seed...")
        
        User.query.delete()
        ClothingItem.query.delete()
        Closet.query.delete()
        
        print("Creating users...")
        
        user_list = []
        
        for _ in range(3):
            new_user = User(name=fake.name(),
                            username=fake.first_name(),
                            password=fake.word())
            user_list.append(new_user)
        # db.session.add_all(user_list)
        # db.session.commit()
        
        
        print("Creating clothing items...")
        


        clothing_items_list = [
            # Tops
            ClothingItem(name="Long Sleeve", 
                         image_url="/images/clothes/longsleeve.jpg", 
                         category="Tops", 
                         tags="cold"
                         ),
            
            ClothingItem(name="T-Shirt", 
                         image_url="/images/clothes/tshirt.jpg", 
                         category="Tops", 
                         tags= "hot"
                         ),
            
            ClothingItem(name="Blouse", 
                         image_url="/images/clothes/blouse.jpg", 
                         category="Tops", 
                         tags="comfortable"
                         ),

            # Bottoms
            ClothingItem(name="Jeans", 
                         image_url="/images/clothes/jeans.jpg", 
                         category="Bottoms", 
                         tags="cold"
                         ),
            
            ClothingItem(name="Shorts", 
                         image_url="/images/clothes/shorts.jpg", 
                         category="Bottoms", 
                         tags="hot"
                         ),
            
            ClothingItem(name="Long Skirt", 
                         image_url="/images/clothes/longskirt.jpg", 
                         category="Bottoms", 
                         tags="comfortable"
                         ),

            # Footwear
            ClothingItem(name="Boots", 
                         image_url="/images/clothes/boots.jpg", 
                         category="Footwear", 
                         tags="cold"
                         ),
            ClothingItem(name="Sneakers", 
                         image_url="/images/clothes/sneakers.jpg", 
                         category="Footwear", 
                         tags="hot"
                         ),

            ClothingItem(name="Mules", 
                         image_url="/images/clothes/mules.jpg", 
                         category="Footwear", 
                         tags="comfortable"
                         ),

            # Outerwear
            # ClothingItem(name="Cardigan", 
            #              image_url="/images/clothes/cardigan.jpg", 
            #              category="Outerwear", 
            #              tags="comfortable"
            #              ),
            
            ClothingItem(name="Sweater", 
                         image_url="/images/clothes/sweater.jpg", 
                         category="Outerwear", 
                         tags="cold"
                         ),
            
            ClothingItem(name="Jacket", 
                         image_url="/images/clothes/jacket.jpg", 
                         category="Outerwear", 
                         tags="cold"
                         ),
        ]

# Add clothing items to your database (you need to implement this part)
# Example code to add items to a SQLAlchemy database:
# for item in clothing_items_list:
#     db.session.add(item)
# db.session.commit()
   
    

        # clothing_items_list = []
        # for _ in range(10):
            
        #     possible_tags = ["hot", "cold", "comfortable"]
            
        #     image_width = 200
        #     image_height = 200
        #     image_url = f"https://picsum.photos/{image_width}/{image_height}"
        #     new_clothing_item = ClothingItem(name = fake.name(),
        #                                 image_url = image_url,
        #                                 category = fake.company(),
        #                                 tags = random.choice(possible_tags))
            
        #     clothing_items_list.append(new_clothing_item)
        # db.session.add_all(clothing_items_list)
        # db.session.commit()
        
    
        
    
        print("Staging all instantiated data...")
        
        db.session.add_all(user_list)
        db.session.add_all(clothing_items_list)
        db.session.commit()
        
        print("Seeding... done!")
        