from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    created = fields.DateTime(dump_only=True)
    updated = fields.DateTime(dump_only=True)
    deleted = fields.DateTime(dump_only=True)


class DisplayUserSchema(Schema):
    username = fields.Str()
    email = fields.Email()
