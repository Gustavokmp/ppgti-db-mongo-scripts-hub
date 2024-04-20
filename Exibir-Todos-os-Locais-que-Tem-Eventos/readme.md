### Consulta: Exibir Todos os Locais que Têm Eventos

- **`$lookup:`** Realiza uma junção entre duas coleções no MongoDB, combinando documentos de uma coleção com documentos de outra coleção com base em uma condição específica.

- **`from: "eventosJP"`:** Especifica a coleção da qual queremos trazer os documentos para combinar com os documentos da coleção atual (`locaisJP`). Neste caso, buscamos os documentos da coleção `eventosJP`.

- **`localField: "_id"`:** Indica o campo na coleção atual (`locaisJP`) que será usado para fazer a correspondência com os documentos da coleção especificada em `from`. Aqui, usamos o campo `_id` da coleção `locaisJP`.

- **`foreignField: "local_id"`:** Indica o campo na coleção especificada em `from` que será usado para fazer a correspondência com os documentos da coleção atual. Neste caso, usamos o campo `local_id` da coleção `eventosJP`.

- **`as: "eventos"`:** Define o nome do novo campo onde os resultados da junção serão armazenados na coleção atual (`locaisJP`). Os documentos combinados da coleção `eventosJP` são armazenados neste novo campo chamado `eventos` dentro dos documentos da coleção `locaisJP`.
