import ctypes
ctypes.cast(orig, ctypes.py_object).value

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    ckpt_path = tf.train.latest_checkpoint('./save')
    saver.restore(sess, ckpt_path)
    #test_loss = sess.run(loss, feed_dict={X: data_test, Y: label_test})
    #print('test loss:', test_loss)
    #test_accuracy = sess.run(acc, feed_dict={X: data_test, Y: label_test})
    #print('test accuracy:', test_accuracy)
    #pred_label = sess.run(tf.argmax(pred, 1), feed_dict={X: data_test, Y: label_test})
    #print(pred_label, label_test)
    X_embedding_val, Y_embedding_val = sess.run([X_embedding, Y_embedding], feed_dict={X: data_test,
