db.locaisJP.aggregate([
    {
        $geoNear: {
            near: { type: "Point", coordinates: [-34.8829, -7.1153] },
            distanceField: "distancia",
            maxDistance: 2000,
            spherical: true
        }
    }
])
