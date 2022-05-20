import boto3
from botocore.exceptions import ClientError

def obtener_bytes_imagen(ruta_imagen):
    with open(ruta_imagen, "rb") as imagen:
        return imagen.read()

def comparar_rostros(ruta_imagen1,ruta_imagen2):
    bytes_1 = obtener_bytes_imagen(ruta_imagen1)
    bytes_2 = obtener_bytes_imagen(ruta_imagen2)

    cliente = boto3.client('rekognition')
    try:
        respuesta = cliente.compare_faces(SourceImage = {'Bytes' : bytes_1},
                                          TargetImage = {'Bytes': bytes_2},
                                          SimilarityThreshold = 0,
                                          QualityFilter = 'NONE')
        if respuesta and respuesta['ResponseMetadata']['HTTPStatusCode'] == 200:
            """ for i in respuesta['UnmatchedFaces']:
                print(i,'\n')
                return 'No es la misma persona' """

            for i in respuesta['FaceMatches']:
                if i['Similarity']>=70:
                    print('Similarity: ' + str(i['Similarity']))
                    porcentaje = str(i['Similarity'])
                    return '  Si es la misma persona \n  Semejanza: ' + porcentaje[0:4] + '%'
                else:
                    print('No es la misma persona, Semajanza: ' + str(i['Similarity']))
                    return '  No es la misma persona'
    except ClientError as error:
        print("Ocurrio un error al llamar a la API:",error)

""" if __name__ == "__main__":
    ruta_imagen_1 = './Imagenes/cadillo.jpg'
    ruta_imagen_2 = './Imagenes/cadillo_dni.jpg'

    comparar_rostros(ruta_imagen_1,ruta_imagen_2) """