import tensorflow as tf
a = tf.constant("Hello, world!", dtype=None, shape=None, name='Const')
sess = tf.Session()
print(sess.run(a))