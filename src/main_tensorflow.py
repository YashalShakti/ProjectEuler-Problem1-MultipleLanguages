# For showing progress
import sys as sys

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

# For the actual neural net
import numpy as np
import tensorflow as tf

def binary_encode(i, num_digits):
    return np.array([i >> d & 1 for d in range(num_digits)])

def euler_encode(i):
    if i % 3 == 0 or i % 5 == 0:
        return np.array([0, 1])
    else:
        return np.array([1, 0])

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))

def model(X, w_h, w_o):
    h = tf.nn.relu(tf.matmul(X, w_h))
    return tf.matmul(h, w_o)

def euler(i, prediction):
    if i % 3 == 0 or i % 5 == 0:
        if prediction == 1:
            print(i)
            return 1
        else:
            return 0
    else:
        if prediction == 0:
            return 1
        else:
            return 0

def main():
    NUM_DIGITS = 10
    NUM_HIDDEN = 100
    BATCH_SIZE = 128

    trX = np.array([binary_encode(i, NUM_DIGITS) for i in range(101, 2 ** NUM_DIGITS)])

    trY = np.array([euler_encode(i) for i in range(101, 2 ** NUM_DIGITS)])

    X = tf.placeholder("float", [None, NUM_DIGITS])
    Y = tf.placeholder("float", [None, 2])

    w_h = init_weights([NUM_DIGITS, NUM_HIDDEN])
    w_o = init_weights([NUM_HIDDEN, 2])

    py_x = model(X, w_h, w_o)

    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(py_x, Y))
    train_op = tf.train.GradientDescentOptimizer(0.05).minimize(cost)

    predict_op = tf.argmax(py_x, 1)

    with tf.Session() as sess:
        tf.initialize_all_variables().run()

        print("Training the neural network")
        maxArgs = 10000
        progress(0, maxArgs)
        for epoch in range(maxArgs):

            p = np.random.permutation(range(len(trX)))
            trX, trY = trX[p], trY[p]

            for start in range(0, len(trX), BATCH_SIZE):
                end = start + BATCH_SIZE
                sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end]})
            progress(epoch, maxArgs)
            #  print(epoch, np.mean(np.argmax(trY, axis=1) == sess.run(predict_op, feed_dict={X: trX, Y: trY})))

        while True:
            start = int(input("\nEnter the start limit or 0 to exit: "))
            if start == 0:
                break
            end = int(input("Enter the end limit: "))
            numbers = np.arange(start, end)
            teX = np.transpose(binary_encode(numbers, NUM_DIGITS))
            teY = sess.run(predict_op, feed_dict={X: teX})
            print("The divisors are: ")
            output = np.vectorize(euler)(numbers, teY)
            accuracy = 0
            for i in output:
                if i == 1:
                    accuracy += 1
            print("Accuracy: ")
            print(accuracy / (len(output)))
            # Show some of the tiny results
            if (end - start <= 10):
                for i in range(start, end):
                    if output[i - start] == 1:
                        sym = u'\u2713'
                    else:
                        sym = u'\u2716'
                    print("(" + str(i) + "," + sym + ")", end=" ; ")
        sess.close()

if __name__ == '__main__':
    main()
