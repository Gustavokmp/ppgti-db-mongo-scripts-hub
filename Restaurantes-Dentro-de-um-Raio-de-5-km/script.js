db.locaisJP.find({
    "localizacao.coordinates": {
        $geoWithin: {
            $centerSphere: [[-34.8829, -7.1153], 5 / 6378.1]
        }
    },
    categoria: "Restaurante"
})
