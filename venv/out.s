.data
	true: .byte 1
	false: .byte 0
	str0: .asciiz "yes"
.text
main:
	li $s0, 1
	li $s1, 2
	li $s2, 3
L0:
	la $t0, false
	ble $s0, $s1, SKIP0
	la $t0, true
SKIP0:
	la $t1, false
	ble $s2, $s1, SKIP1
	la $t1, true
SKIP1:
	and $t2, $t0, $t1
	la $t3, true
	beq $t3, $t2, if0
L1:
	j END
if0:
	li $v0, 4
	la $a0, str0
	syscall
	j L1
END:
