import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Staff as StaffModel, DepartmentRef as DepartmentRefModel

'''
■エンドポイント定義

・リクエスト例
{
  allStaff {
    edges {
      node {
        id
        name
        branch
      }
    }
  }
}
{
  allDepartment {
    edges {
      node {
        id
        departmentName
        staffId
      }
    }
  }
}
'''
class Staff(SQLAlchemyObjectType):
    class Meta:
        model = StaffModel
        interfaces = (relay.Node, )

class DepartmentRef(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentRefModel
        interfaces = (relay.Node, )

"""
class StaffConnection(relay.Connection):
    class Meta:
        node = Staff
"""

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_staff = SQLAlchemyConnectionField(Staff)
    all_department = SQLAlchemyConnectionField(DepartmentRef)
    #all_staff_departments = SQLAlchemyConnectionField(StaffConnection)

schema = graphene.Schema(query=Query)