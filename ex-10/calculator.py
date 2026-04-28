
(format t "Enter first number: ")
(setq a (read))

(format t "Enter second number: ")
(setq b (read))

(format t "~%Choose operation:
 +  (Addition)
 -  (Subtraction)
 *  (Multiplication)
 /  (Division)
 %  (Modulus)
 p  (Power a^b)
 m  (Maximum)
 n  (Minimum)
: ")

(setq op (read))

(cond
  ((eq op '+) (format t "~%Result: ~A" (+ a b)))
  ((eq op '-) (format t "~%Result: ~A" (- a b)))
  ((eq op '*) (format t "~%Result: ~A" (* a b)))
  ((eq op '/) (format t "~%Result: ~A" (/ a b)))
  ((eq op '%) (format t "~%Result: ~A" (mod a b)))
  ((eq op 'p) (format t "~%Result: ~A" (expt a b)))
  ((eq op 'm) (format t "~%Maximum: ~A" (max a b)))
  ((eq op 'n) (format t "~%Minimum: ~A" (min a b)))
  (t (format t "~%Invalid operation")))
