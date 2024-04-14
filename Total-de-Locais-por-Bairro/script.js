db.locaisJP.aggregate([
    {
        $group: {
            _id: "$bairro",
            total: { $sum: 1 }
        }
    }
])
