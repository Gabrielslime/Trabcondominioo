const express = require('express');
const bodyParser = require('body-parser');
const sequelize = require('./config/database');
const City = require('./models/City');
const Customer = require('./models/Customer');
const Order = require('./models/Order');
const OrderProduct = require('./models/OrderProduct');
const Product = require('./models/Product');
const Category = require('./models/Category');

const app = express();
app.use(bodyParser.json());

sequelize.sync().then(() => console.log('Banco de dados sincronizado'));

app.get('/products', async (req, res) => {
  const products = await Product.findAll();
  res.json(products);
});

app.post('/orders', async (req, res) => {
  const { datetime, address, customerId, products } = req.body;

  try {
    const order = await Order.create({ datetime, address, customerId });
    await Promise.all(products.map(async (product) => {
      await OrderProduct.create({
        orderId: order.id,
        productId: product.productId,
        price: product.price,
        quantity: product.quantity
      });
    }));
    res.status(201).json(order);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.get('/orders', async (req, res) => {
  const orders = await Order.findAll();
  res.json(orders);
});

app.post('/products', async (req, res) => {
  try {
    const product = await Product.create(req.body);
    res.status(201).json(product);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.put('/products/:id', async (req, res) => {
  try {
    await Product.update(req.body, { where: { id: req.params.id } });
    res.status(200).json({ message: 'Produto atualizado com sucesso' });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.delete('/products/:id', async (req, res) => {
  try {
    await Product.destroy({ where: { id: req.params.id } });
    res.status(200).json({ message: 'Produto excluído com sucesso' });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.delete('/orders/:id', async (req, res) => {
  try {
    await Order.destroy({ where: { id: req.params.id } });
    res.status(200).json({ message: 'Pedido excluído com sucesso' });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));