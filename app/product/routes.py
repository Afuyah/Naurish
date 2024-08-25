from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from app.main.forms import AddProductForm
from app.product import product_bp
from app import db, admin_required
from app.main.models import PriceHistory, Product

@product_bp.route('/products', methods=['GET'])
@admin_required
def products():
    products = Product.query.all()  
    return render_template('products_page.html', products=products)

@product_bp.route('/products/<int:product_id>/manage', methods=['GET'])
@admin_required
def manage_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = AddProductForm(obj=product)  # Pass the product to populate the form
    return render_template('manage_product.html', product=product, form=form)

@product_bp.route('/products/<int:product_id>', methods=['GET'])
@admin_required
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'unit_price': product.unit_price,
        'discount_percentage': product.discount_percentage,
        'quantity_in_stock': product.quantity_in_stock,
        'country_of_origin': product.country_of_origin,
        'brand': product.brand,
        'nutritional_information': product.nutritional_information,
        'supplier_id': product.supplier_id,
        'category_id': product.category_id,
        'unit_measurement_id': product.unit_measurement_id
    })

@product_bp.route('/products/update/price', methods=['POST'])
@admin_required
def update_price():
    data = request.form
    product_id = int(data.get('product_id'))
    new_price = float(data.get('new_price'))
    product = Product.query.get_or_404(product_id)

    old_price = product.unit_price
    product.unit_price = new_price

    # Recalculate the selling price based on the new unit price
    product.calculate_selling_price()

    # Record price history
    if old_price != product.unit_price:
        price_history = PriceHistory(product_id=product.id, old_price=old_price, new_price=product.unit_price)
        db.session.add(price_history)

    db.session.commit()
    return jsonify({'success': True})

@product_bp.route('/products/update/discount', methods=['POST'])
@admin_required
def update_discount():
    data = request.form
    product_id = int(data.get('product_id'))
    discount_percentage = float(data.get('discount_percentage'))
    product = Product.query.get_or_404(product_id)

    # Update the discount percentage
    product.discount_percentage = discount_percentage

    # Recalculate the selling price
    if product.unit_price > 0:
        discount_amount = (discount_percentage / 100) * product.unit_price
        product.selling_price = product.unit_price - discount_amount

    # Commit the changes to the database
    db.session.commit()

    return jsonify({'success': True})


@product_bp.route('/products/update/quantity', methods=['POST'])
@admin_required
def update_quantity():
    data = request.form
    product_id = int(data.get('product_id'))
    additional_quantity = int(data.get('quantity_in_stock'))
    
    # Fetch the product and update its quantity
    product = Product.query.get_or_404(product_id)
    product.quantity_in_stock += additional_quantity
    
    # Commit the changes to the database
    db.session.commit()
    
    # Return a JSON response indicating success
    return jsonify({'success': True})


@product_bp.route('/products/update/country', methods=['POST'])
@admin_required
def update_country():
    data = request.form
    product_id = int(data.get('product_id'))
    country_of_origin = data.get('country_of_origin')
    product = Product.query.get_or_404(product_id)
    product.country_of_origin = country_of_origin
    db.session.commit()
    return jsonify({'success': True})

@product_bp.route('/products/update/name', methods=['POST'])
@admin_required
def update_product_name():
    product_id = request.form['product_id']
    new_name = request.form['name']
    product = Product.query.get(product_id)
    if product:
        product.name = new_name
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False)

@product_bp.route('/products/update/brand', methods=['POST'])
@admin_required
def update_product_brand():
    product_id = request.form['product_id']
    new_brand = request.form['brand']
    product = Product.query.get(product_id)
    if product:
        product.brand = new_brand
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False)

@product_bp.route('/products/update/nutrition', methods=['POST'])
@admin_required
def update_product_nutrition():
    product_id = request.form['product_id']
    new_nutrition = request.form['nutritional_information']
    product = Product.query.get(product_id)
    if product:
        product.nutritional_information = new_nutrition
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False)




