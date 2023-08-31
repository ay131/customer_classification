# customer_classification
odoo15 comunity module

A new Add-on on odoo 15 that do the following :
1- Define a new entity called customer.classification so that the user can add/edit/delete classfication list 
2- Classfication model consist of the following attributes: title and score
3- All edit operations on previous fields sould be tracked on the chatter.
4- classification can be accessed from configration menu in contact application
5- Add new field to customer model so that the admin can assign classification to customer based on the previous list
6- Update sales dashboard (from sales application --> reporting menu --> sales) so that we can view report based on customer classification measure
7- Update sale order creation form so that when the admin choose a customer with score more that 70 he will get a discount = 1% of the total order amount.
8- build a json based API that Accept POST requests, return a list of all classifications defined in the system and can be invoked via external systems using shared API key
![image](https://github.com/ay131/customer_classification/assets/24198990/351817e6-3953-40c1-b568-75dc766c9cbe)

