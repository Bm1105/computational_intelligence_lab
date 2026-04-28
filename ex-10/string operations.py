(defun count-vowels (str)
  (let ((count 0))
    (loop for ch across str do
         (when (find ch "aeiouAEIOU")
           (incf count)))
    count))

(defun main ()
  (format t "Enter a string: ")
  (let ((input (read-line)))

    ;; Length
    (format t "~%Length: ~A" (length input))

    ;; Reverse
    (format t "~%Reverse: ~A"
            (coerce (reverse (coerce input 'list)) 'string))

    ;; Uppercase
    (format t "~%Uppercase: ~A" (string-upcase input))

    ;; Lowercase
    (format t "~%Lowercase: ~A" (string-downcase input))

    ;; Vowel count
    (format t "~%Vowel Count: ~A" (count-vowels input))

    (terpri)))

(main)
