import time

from rest_framework.exceptions import ValidationError


def get_products():
    """
    Get products from database
    :return: list of products
    """

    products = [
        {
            "name": "Apple Macbook Air M1",
            "id": 1,
            "price": 1000
        },
        {
            "name": "Apple Macbook Air M2",
            "id": 2,
            "price": 1500
        },
        {
            "name": "Apple Macbook Pro M1",
            "id": 3,
            "price": 1300
        },
        {
            "name": "Apple Macbook Pro M2",
            "id": 4,
            "price": 2000
        }
    ]
    return products


def get_product_by_id(product_id):
    """
    Returns product by id
    :param product_id: ID of the product
    :return: product instance
    """

    for product in get_products():
        if product.get("id") == product_id:
            return product
    raise ValidationError("Product not found")
