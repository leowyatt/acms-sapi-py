import graphene
import acms.schema

class Query(acms.schema.Query, graphene.ObjectType):
    pass

class Mutation(acms.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)