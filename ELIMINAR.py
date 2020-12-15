# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:07:38 2020

@author: DIANA
"""
import sqlite3
conexion = sqlite3.connect("bdpruebita.db")
cursor = conexion.cursor()
consulta = """
            UPDATE EDITORIAL
            SET
                NOMBRE = 'EIU'
            WHERE
                IDEDITORIAL = 1
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close() 

