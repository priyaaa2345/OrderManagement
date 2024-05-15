create table Product(
    productId int,
    productName varchar(255),
    description varchar(255),
    price int,
    quantityInStock int,
    type varchar(255)
);
create table Electronics(brand text, warrantyPeriod int);
insert into Electronics
values('hcl', 2),
    ('apple', 3),
    ('samsung', 2),
    ('poco', 1);
create table Clothing(size char, color text);
CREATE TABLE Users (
    userId INT,
    username VARCHAR(255),
    password VARCHAR(255),
    role TEXT
);
CREATE TABLE Orders (
    orderId INTEGER,
    userId INTEGER NOT NULL,
);