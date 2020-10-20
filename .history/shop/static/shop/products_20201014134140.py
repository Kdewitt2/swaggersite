from jinja2 import Template



products = {
    "Grapefruit Soap": {1, 8.99, "Bright, citrus soap made with Shea Butter, Mango Butter, and Cocoa Butter to moisturize the skin. This soap has a drizzle of Grapefruit essential oil.", "#soap#grapefruit#organic"},
    "Lemongrass Sugar Scrub": {2, 10.99, "It's a sugar scrub with character. Bright lemon smell that leaves your face felling like a million bucks.", "'#sugarscrub#lemon#organic"},
    "Charcoal & Clay Facial Scrub": {3, 10.99, "Face scrub that unclogs your pores and cleanses your face.", "#charcoal#clay#facialscrub#organic"},
    "Lavender Soap": {4, 8.99, "A soft soap with a lovely scent of lavender and vanilla.", "#lavender#soap#organic"},
    "Aloe Vera & Goat Milk Soap": {5, 9.99, "A very nice blend of cleansing aloe and softening goat milk.", "#aloe#aloevera#goatmilk#soap"},
    "Peppermint Soap": {6, 8.99, "Cleanses your skin and fills it with a pepermint sensation.", "#peppermint#soap#organic"},
    "Eucalyptus Soap": {7, 8.99, "Opens your poors and gives you a cool, smooth feeling.", "#eucalyptus#soap#organic"},
    "Raw Soap": {8, 7.99, "Mild, organic, scentless soap for those who want a gentle clean without any added color or fragrance.", "#raw#scentless#organic"},
    "Calendula Burdock Salve": {9, 10.99, "An effective moisturizing salve made with an infusion of calendula, burdock root, and lavender.", ""},
    "Soothe Me Salve": {10, 10.99, "A healing and moisturising salve made with an infusion of Comfrey, Calendula, Rose, Rosemary, and Plantain.", "#salve#comfrey#calendula#rose#rosemary#plantain#organic"},
    "Lavender Loofah Soap": {11, 8.99, "Lavender Soap with a Loofah inside to help scrub the bad away.", "#soap#lavender#loofah"}
}