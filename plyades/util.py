from __future__ import division
import re
import numpy as np

def rot(angle, axis=3):
	'''

	'''
	M = np.zeros((3,3))
	if axis == 1:
		M[0,0] = 1
		M[1,1] = np.cos(angle)
		M[1,2] = np.sin(angle)
		M[2,1] = -np.sin(angle)
		M[2,2] = np.cos(angle)
		return M
	elif axis == 2:
		M[0,0] = np.cos(angle)
		M[0,2] = -np.sin(angle)
		M[1,1] = 1
		M[2,0] = np.sin(angle)
		M[2,2] = np.cos(angle)
		return M
	elif axis == 3:
		M[0,0] = np.cos(angle)
		M[0,1] = np.sin(angle)
		M[1,0] = -np.sin(angle)
		M[1,1] = np.cos(angle)
		M[2,2] = 1
		return M

def rotd(angle, angular_velocity, axis=3):
	M = np.zeros((3,3))
	if axis == 1:
		M[1,1] = -angular_velocity * np.sin(angle)
		M[1,2] = angular_velocity * np.cos(angle)
		M[2,1] = -angular_velocity * np.cos(angle)
		M[2,2] = -angular_velocity * np.sin(angle)
		return M
	elif axis == 2:
		M[0,0] = -angular_velocity * np.sin(angle)
		M[0,2] = -angular_velocity * np.cos(angle)
		M[2,0] = angular_velocity * np.cos(angle)
		M[2,2] = -angular_velocity * np.sin(angle)
		return M
	elif axis == 3:
		M[0,0] = -angular_velocity * np.sin(angle)
		M[0,1] = angular_velocity * np.cos(angle)
		M[1,0] = -angular_velocity * np.cos(angle)
		M[1,1] = -angular_velocity * np.sin(angle)
		return M
		
def euler(alpha, beta, gamma, order="321"):
	
	# Input checking.
	reg = re.compile("[1-3][1-3][1-3]")
	if not reg.match(order) and len(order) > 3:
		raise ValueError("Incorrect rotation order definition.")
	
	m_alpha = rot(alpha, axis=int(order[0]))
	m_beta = rot(beta, axis=int(order[1]))
	m_gamma = rot(gamma, axis=int(order[2]))
	return np.dot(m_alpha, np.dot(m_beta, m_gamma))

def dms2rad(degrees, minutes, seconds):
	return (degrees + minutes/60 + seconds/3600) * np.pi/180

def hms2rad(degrees, minutes, seconds):
	return (degrees + minutes/60 + seconds/3600) * 15 * np.pi/180