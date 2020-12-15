# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:42:52 2020

@author: osito
"""
# Crear Tablas
import sqlite3
conexion = sqlite3.connect("bdpruebita.db")

tabla_pais =    """ CREATE TABLE PAIS(
                    IDPAIS INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE TEXT UNIQUE,
                    ESTADO TEXT
                )                
                """

tabla_editorial = """ CREATE TABLE EDITORIAL(
                    IDEDITORIAL INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE TEXT UNIQUE,
                    ESTADO TEXT
                )                
                """

tabla_autor =    """ CREATE TABLE AUTOR(
                    IDAUTOR INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE TEXT UNIQUE,
                    F_NACIMIENTO TEXT,
                    ESTADO TEXT
                )                
                """
            
cursor = conexion.cursor()
cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)

conexion.close()
