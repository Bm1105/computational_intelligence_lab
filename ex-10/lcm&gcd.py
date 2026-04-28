
(defun gcd-func (a b)
  (if (= b 0)
      a
      (gcd-func b (mod a b))))

(defun lcm-func (a b)
  (/ (* a b) (gcd-func a b)))

(format t "Enter two integers: ")
(let ((a (read)) (b (read)))
  (format t "~%GCD: ~A" (gcd-func a b))
  (format t "~%LCM: ~A" (lcm-func a b)))
